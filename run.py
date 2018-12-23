from flask import Flask, request, redirect, jsonify
from flask_pymongo import PyMongo
from dbfunctions import *
from bson.objectid import ObjectId
import pprint
app = Flask(__name__)



@app.route('/list_all_emp',methods=['GET','POST'])
def list_all_emp():
	if request.method=='POST':
		form=request.form
		result=find_all_in_collection('employee_data')
		print "\n\n",pprint.pprint(result),"\n\n"
		for i in range(0,len(result)):
				result[i].pop('_id',None)
		if "view_type" in form:
		# if form['view_type']=="address":
			for i in range(0,len(result)):
				result[i].pop('l_name',None)
				result[i].pop('f_name',None)
				result[i].pop('dob',None)

		if "emp_id" in form:
			for i in result:
				if (i['emp_id'] !=	form["emp_id"] ):
					result.remove(i)


		print result

	return jsonify(result)

@app.route('/del_emp_by_id',methods=['GET','POST'])
def del_emp_by_id():
	if request.method=='POST':
		print "\n\ndawuidjaowid\n\nUHFEOIFJAEOI"
		form=request.form
		result=del_doc('employee_data',{"emp_id":form['emp_id']})
	return jsonify(result)


@app.route('/add_emp',methods=['GET','POST'])
def add_emp():
	if request.method=='POST':
		form=request.form
		f_name=form['f_name']
		l_name=form['l_name']
		dob=form['dob']
		addr_type=form['addr_type']
		addr=form['addr']
		emp_id=form['emp_id']		
		result=find_and_filter('employee_data',{"emp_id":emp_id})
		print "\n\n",result,"\n\n"

		if addr_type not in ['present','permanent','office']:
			return "Please Engter RIght Address Type"

		if len(result)==0:
			addr={addr_type:addr}
			save_collection("employee_data",{"emp_id":emp_id,"f_name":f_name,"l_name":l_name,"dob":dob,"addr":addr})
			return "Saved New Employee"
		else:
			addr_dict={}
			addr_dict=result[0]['addr']
			addr_dict[addr_type]=addr
			update_dict={"emp_id":emp_id,"f_name":f_name,"l_name":l_name,"dob":dob,"addr":addr_dict}

			update_collection("employee_data",{"emp_id":emp_id},{"$set":update_dict})
			return "Employee Updated"

if __name__ == '__main__':
	# app.run(debug=True)
    app.run(host='0.0.0.0', port=1111,debug=True)

