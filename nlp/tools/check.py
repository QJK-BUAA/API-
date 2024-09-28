from llms import deepseek
from docx import Document
from prompts import prompt_temple

class DocumentChecker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.document = Document(file_path)

    def check_pronunciation(self, prompt):
        for para in self.document.paragraphs:
            text = para.text
            feedback = deepseek.get_response(f"{prompt}：{text}")
            para.text += f"\n反馈：{feedback}"

    def save_document(self, new_file_path):
        self.document.save(new_file_path)


class Student(DocumentChecker):
    def review_document(self):
        student_prompt = prompt_temple.prompt_student
        self.check_pronunciation(student_prompt)
        self.save_document('student_reviewed.docx')


class Teacher(DocumentChecker):
    def review_document(self):
        teacher_prompt = prompt_temple.prompt_teacher
        self.check_pronunciation(teacher_prompt)
        self.save_document('teacher_reviewed.docx')