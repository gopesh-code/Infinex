# Infinex

## Overview

**Infinex** is a Django-based web application that simplifies the college application process for students across the country. It provides modules for both students and administrators, enabling easy submission, storage, and management of application documents. The platform aims to streamline the submission process, helping students track deadlines and ensure their applications are complete.

## Features

### User Side

- **View College Lists**: Access a curated list of colleges and their application procedures, including important deadlines.
- **Application Submission**: Submit a comprehensive application form with all necessary documents for various colleges.
- **Document Storage**: Securely store and manage important documents, allowing for easy access and retrieval when needed.

- View college lists: This functionality is one of the most crucial ones offered by our web application Infinex. Students can view different colleges’ application procedures and amount payable for the same. It is found that many times students are not able to fill up the college forms on time. Hence, this feature allows them to be up to dae about the deadlines and required documents, processes for application submission. We try to include many popular colleges’ entrance application forms such as BITSAT, VITEEE, JEE, etc. This can be updated by the admin/superuser of Infinex for conveying specific information.
  
- Application submission: It is found that submitting various documents together can create chaos and often some important documents are not submitted. We try to remove this chaos by creating a common form for all the necessary documents required by the students while filling a college application. After surveying 20 colleges’ application procedures we noted down the common documents for all these colleges and supplied a unique interface to store them. Not only document submission but users can submit them for approval of the admin and determine whether a particular candidate is suitable for the applied colleges or not.
  
- Document storage: After filling Infinex application form, users can verify their details, view and edit them accordingly. If a user requires a particular document they can download the same. This collectively reduces the time taken to gather documents. Hence this functionality benefits the user in two ways, first it acts as a storage portal and secondly improves the efficiency of document collection.

### Admin Side

- **Application Review**: Admins can verify submitted documents and provide feedback.
- **Application Approval/Denial**: Review and update the status of each application based on document accuracy and completeness.
- **Manage College Information**: Update college admission procedures and deadlines for students to view.

- Updating application status: Admin has access to the applications sent in by users. He/she can accordingly review the form and verify whether the student is eligible for the particular college. This helps students in getting an idea regarding the chances of successful entry in that college. Admin can also add comments to help students get feedback regarding their documents.
  
- Approval of applications: With the number of high candidates in every competitive exam, it is natural that some applications are going to be rejected if the details are not appropriate. Admin can reject or approve the application and users can view their status accordingly. The interface for admin allows to easily place and view rejected as well as approved documents. The documents yet to be verified are in the pending category.
  
- Viewing submitted documents: Documents are verified by the admin and if there are any discrepancies, the admin can convey the same information to the user. This allows for verification of the documents and helps in the application procedure. Updating college application procedure: To help the students understand various college admission processes and approaching deadlines, this functionality displays the procedure conveniently and in layman terms. This allows students from all walks of life to participate in the admissions.

  
## Technologies Used

- **Python**: Backend logic with Django.
- **HTML/CSS**: Front-end design and layout.
- **SQLite**: Database for storing user and application data.

## Installation

1. **Clone the repository**:
  ```bash
  git clone https://github.com/gopesh-code/Infinex.git
  cd Infinex
  ```
2. **Set up virtual environment**:
  ```bash
  python -m venv env
  source env/bin/activate  # For Windows: env\\Scripts\\activate
  ```
3. **Install Dependencies**:
  ```bash
  pip install -r requirements.txt
  ```
4. **Run the application**:
  ```bash
  python manage.py runserver
  ```
5. **Access the application: Open a browser and go to http://localhost:8000.**

## File Structure

```plaintext
├── collegeportal/          # Main Django application code
├── static/                 # Static files (CSS, JavaScript)
├── templates/              # HTML templates
├── db.sqlite3              # Database file
├── manage.py               # Django management script
├── requirements.txt        # Dependencies
└── README.md               # This file
```

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
