def admission_list(applicant_list, max_admitted):
    accepted = {}
    for course in range(7, 10):

        ranking = {}
        for student in applicant_list:
            for department in student.split()[7:10]:
                ranking[department] = ranking.get(department, []) + [student]

        for department in ranking.keys():
            if department not in accepted:
                accepted[department] = []

            score_aux = course_aux[department] if department in ("Physics", "Biotech", "Engineering") else None

            for index, student in enumerate(ranking[department]):
                if score_aux:
                    admission_score = max((float(student.split()[course_col[department]]) + float(student.split()[score_aux])) / 2, float(student.split()[6]))

                else:
                    admission_score = max(float(student.split()[course_col[department]]), float(student.split()[6]))

                ranking[department][index] = student + " " + str(admission_score)

            applicants = sorted(sorted(ranking[department], key=lambda x: x.split()[0] + x.split()[1]), key=lambda x: x.split()[10], reverse=True)

            for i in range(len(applicants)):
                if applicants[i].split()[course] == department and len(accepted[department]) < max_admitted:
                    accepted[department].append(applicants[i])

        candidates = [" ".join(p.split()[:10]) for department in accepted.keys() for p in accepted[department]]
        applicant_list = [student for student in applicant_list if student not in candidates]

    return accepted


def save(admitted):
    for dept in admitted.keys():
        score = ''

        if dept in ("Physics", "Biotech", "Engineering"):
            score = course_aux[dept]

        with open(f"{dept.lower()}.txt", 'w') as file:
            for applicant in sorted(sorted(admitted[dept], key=lambda x: x.split()[0] + x.split()[1]), key=lambda x: x.split()[10], reverse=True):
                if score:
                    final = max(float(applicant.split()[6]), (float(applicant.split()[course_col[dept]]) + float(applicant.split()[score])) / 2)

                else:
                    final = max(float(applicant.split()[6]), float(applicant.split()[course_col[dept]]))

                file.write(" ".join([f"{applicant.split()[0]} {applicant.split()[1]}", str(final)]) + "\n")


course_col = {"Physics": 2, "Chemistry": 3, "Biotech": 3, "Mathematics": 4, "Engineering": 5}
course_aux = {"Physics": 4, "Biotech": 2, "Chemistry": 4, "Engineering": 4, "Mathematics": 4}

with open("applicants.txt") as f:
    data = [line.strip() for line in f.readlines()]

save(admission_list(data, int(input())))
