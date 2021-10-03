from flask import Flask, render_template, redirect
from data_init import collection_budget

app = Flask(__name__)

result = {
}

project_names = []
project_budget = []

def intialize():

    for doc in collection_budget.find():
        if doc["name"] not in result:
            result[doc["name"]] = [0,0,0]
        else:
            result[doc["name"]][0] += doc["totals"]["total_labor"]
            result[doc["name"]][1] += doc["totals"]["total_equipment"]
            result[doc["name"]][2] += doc["totals"]["total_material"]

    for entry in result:
        for element in range(len(result[entry])):
            result[entry][element] = "{:.2f}".format(result[entry][element])

    print(result)

    for entry in result:
        project_names.append(entry)
        project_budget.append(result[entry])

intialize()

@app.route('/')
def home():
    return render_template("main.html", projects = result, project_names = project_names, project_budget = project_budget, individual = project_names[0]) 

@app.route('/<string:name>')
def project(name):
    return render_template("main.html", projects = result, project_names = project_names, project_budget = project_budget, individual = name) 

if __name__=="__main__":
    app.run(debug=True)