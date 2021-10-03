import pymongo
import json
from pymongo import MongoClient

client = MongoClient("mongodb+srv://sam9977:codered1234@cluster0.bsjir.mongodb.net/kpi_proj?retryWrites=true&w=majority", ssl=True,ssl_cert_reqs='CERT_NONE')
db = client["kpi_proj"]
collection_project = db["project"]

with open('data/db.json') as json_file:
    data = json.load(json_file)

# populate project collection

# for project in data["projects"]:
    
#     entry = {
#         "id": project["id"],
#         "name": project["projectName"],
#         "type_work": project["typeOfWork"],
#         "start_date": project["startDate"],
#         "end_date": project["endDate"],
#         "budget": project["budget"],
#         "actual": project["actual"],
#         "timecards": project["timecardIds"],
#         "photo_id": project["photoIds"],
#         "location": project["location"]
#     }

#     collection_project.insert_one(entry)

#----------------------------------------------------------------------------------------------------------

# populate budget collection

collection_budget = db["budget"]

# populates budgets for all projects

# for project in data["projects"]:

#     for budgets in project["budget"]:
        
    
#         entry = {
#             "id": project["id"],
#             "name": project["projectName"],
#             "date": budgets["date"],
#             "budget": budgets,
#             "actual": None,
#             "totals": None,
#         }

#         collection_budget.insert_one(entry)


# populates actuals for the dates and projectNames that match

# for project in data["projects"]:

#     for budgets in project["actual"]:
        
#         query = { "date": budgets["date"], "name": project["projectName"] }

#         newvalues_actual = { "$set": { "actual": budgets } }

#         collection_budget.update_one(query, newvalues_actual)

# # deletes entries with no actuals

# delete_query = {"actual": None}
# collection_budget.delete_many(delete_query)

# calculate totals

# for doc in collection_budget.find():
#     query = { "date": doc["date"], "name": doc["name"] }
#     total_dict = {
#         "total_labor": doc["budget"]["labor"] - doc["actual"]["labor"],
#         "total_equipment":doc["budget"]["equipment"] - doc["actual"]["equipment"],
#         "total_material": doc["budget"]["material"] - doc["actual"]["material"]
#     }
#     new_values_total = { "$set": { "totals": total_dict } }
#     collection_budget.update_one(query, new_values_total)

result = {
}

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









