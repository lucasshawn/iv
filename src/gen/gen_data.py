import json
import random

gen_js = []
def denormalize_string(s):
  if not s: return s
  return s.title() if random.randint(0,1) == 0 else s.lower() if random.randint(0,1) == 0 else s.upper()

for student in range(1,300):
  # each student has three assignments
  assignment_count = random.randint(0,4)
  if not assignment_count: 
    gen_js.append({"student_name":f"student{student}","assignment":None})
  else:
    for assignment in range(1,random.randint(1,4)):
      pass_fail_null = random.randint(0,2)
      pass_fail = "pass" if pass_fail_null == 0 else "fail" if pass_fail_null == 1 else None
      gen_js.append(
        {
          "student_name":f"student{student}",
          "assignment":{
            "name":f"Assignment{assignment}",
            "result":denormalize_string(pass_fail)
          }
        })
gen_js = random.sample(gen_js, k=len(gen_js))
with open("../../data/student_data.json","w") as f:
  f.write(json.dumps(gen_js,indent=2))
