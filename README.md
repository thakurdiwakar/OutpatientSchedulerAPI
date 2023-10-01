

# OutpatientSchedulerAPI

OutpatientSchedulerAPI is a simple API for managing outpatient appointments with doctors. It allows users to:

- Retrieve a list of available doctors.
- Get details about a specific doctor.
- Book an appointment with a doctor.

## Live API Demo

You can try out the live API by following this link: [Live API](https://outpatientschedulerapi-03cx.onrender.com/)

## Getting Started

To get started with this API, follow the instructions below:

### Prerequisites

- Python 3.x
- Flask (install using `pip install Flask`)

### Installation

1. Clone the repository:

```shell
git clone https://github.com/your-username/OutpatientSchedulerAPI.git
cd OutpatientSchedulerAPI
```

2. Run the Flask application:

```shell
python app.py
```

The API should now be running locally on `http://127.0.0.1:5000/`.

## Endpoints

### Get a List of Doctors  
![image](https://github.com/thakurdiwakar/OutpatientSchedulerAPI/assets/76618190/39948684-293e-4822-8dfb-85b292c1d4c2)

- **Endpoint:** `/api/doctors`
- **Method:** GET
- **Description:** Get a list of all available doctors.


### Get Doctor Details

![image](https://github.com/thakurdiwakar/OutpatientSchedulerAPI/assets/76618190/aeefb23a-3236-40ec-aa3d-a1b75a332654)

- **Endpoint:** `/api/doctors/<int:doctor_id>`
- **Method:** GET
- **Description:** Get details about a specific doctor by their ID.

### Book an Appointment

![image](https://github.com/thakurdiwakar/OutpatientSchedulerAPI/assets/76618190/9ac6ddc4-f8e0-457b-99b1-cd92c69fba61)



- **Endpoint:** `/api/appointments`
- **Method:** POST
- **Description:** Book an appointment with a doctor. Provide the doctor ID and desired appointment slot in the request body.

Sample request body:

```json
{
  "doctor_id": 1,
  "slot": {
    "day": "Monday",
    "start_time": "16:00",
    "end_time": "17:00"
  }
}
```

## Example Usage

- To retrieve a list of doctors: `GET /api/doctors`
- To get details about a specific doctor (e.g., with ID 1): `GET /api/doctors/1`
- To book an appointment with a doctor: `POST /api/appointments`



