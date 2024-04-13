-- Indexes for students table
CREATE INDEX "idx_students_id" ON "students"("id");

-- Indexes for courses table
CREATE INDEX "idx_courses_dept_num_sem" ON "courses"("department", "number", "semester");
CREATE INDEX "idx_courses_title_sem" ON "courses"("title", "semester");

-- Indexes for enrollments table
CREATE INDEX "idx_enrollments_student_id" ON "enrollments"("student_id");
CREATE INDEX "idx_enrollments_course_id" ON "enrollments"("course_id");

-- Indexes for satisfies table
CREATE INDEX "idx_satisfies_course_id" ON "satisfies"("course_id");
CREATE INDEX "idx_satisfies_req_id" ON "satisfies"("requirement_id");

-- Indexes for queries involving students and enrollments
CREATE INDEX "idx_enrollments_student_id_course_id" ON "enrollments"("student_id", "course_id");

-- Indexes for queries involving courses and enrollments
CREATE INDEX "idx_enrollments_course_id_student_id" ON "enrollments"("course_id", "student_id");

-- Indexes for queries involving courses and satisfies
CREATE INDEX "idx_satisfies_course_id_req_id" ON "satisfies"("course_id", "requirement_id");

-- Indexes for queries involving requirements and satisfies
CREATE INDEX "idx_satisfies_req_id_course_id" ON "satisfies"("requirement_id", "course_id");
