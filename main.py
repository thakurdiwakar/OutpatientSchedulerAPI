# Import the Flask module, which contains the Flask class for building web applications. This class will be used to build our basic Flask project.

from flask import Flask, request, jsonify

# Create a Flask app instance
app = Flask(__name__)


# Data samples for doctors and appointments
doctors = [
    {
        "id": 1,
        "name": "Dr. Rahul Kapoor",
        "specialty": "Cardiologist",
        "availability": [
            {
                "day": "Monday",
                "start_time": "16:00",
                "end_time": "18:00",
                "remaining_slots": 8
            },
            {
                "day": "Wednesday",
                "start_time": "15:00",
                "end_time": "17:00",
                "remaining_slots": 12
            },
            {
                "day": "Friday",
                "start_time": "14:00",
                "end_time": "16:00",
                "remaining_slots": 10
            }
        ]
    },
    {
        "id": 2,
        "name": "Dr. Nisha Sharma",
        "specialty": "Dermatologist",
        "availability": [
            {
                "day": "Tuesday",
                "start_time": "14:00",
                "end_time": "16:00",
                "remaining_slots": 6
            },
            {
                "day": "Thursday",
                "start_time": "16:00",
                "end_time": "18:00",
                "remaining_slots": 9
            },
            {
                "day": "Saturday",
                "start_time": "11:00",
                "end_time": "13:00",
                "remaining_slots": 7
            }
        ]
    },
    {
        "id": 3,
        "name": "Dr. Anuj Mehta",
        "specialty": "Orthopedic Surgeon",
        "availability": [
            {
                "day": "Monday",
                "start_time": "17:00",
                "end_time": "19:00",
                "remaining_slots": 7
            },
            {
                "day": "Wednesday",
                "start_time": "16:00",
                "end_time": "18:00",
                "remaining_slots": 11
            },
            {
                "day": "Friday",
                "start_time": "15:00",
                "end_time": "17:00",
                "remaining_slots": 9
            }
        ]
    },
    {
        "id": 4,
        "name": "Dr. Priya Gupta",
        "specialty": "Gynecologist",
        "availability": [
            {
                "day": "Tuesday",
                "start_time": "15:00",
                "end_time": "17:00",
                "remaining_slots": 9
            },
            {
                "day": "Thursday",
                "start_time": "14:00",
                "end_time": "16:00",
                "remaining_slots": 12
            },
            {
                "day": "Saturday",
                "start_time": "13:00",
                "end_time": "15:00",
                "remaining_slots": 8
            }
        ]
    },
    {
        "id": 5,
        "name": "Dr. Sanjay Verma",
        "specialty": "Ophthalmologist",
        "availability": [
            {
                "day": "Monday",
                "start_time": "14:00",
                "end_time": "16:00",
                "remaining_slots": 6
            },
            {
                "day": "Wednesday",
                "start_time": "13:00",
                "end_time": "15:00",
                "remaining_slots": 10
            },
            {
                "day": "Friday",
                "start_time": "12:00",
                "end_time": "14:00",
                "remaining_slots": 7
            }
        ]
    },

]

# List to store booked appointments
appointments = []

# Define a route to get a list of all doctors


@app.route("/api/doctors", methods=["GET"])
def get_doctors():
    # Return a JSON response containing a list of all doctors
    return jsonify([doctor for doctor in doctors])

# Define a route to get information about a specific doctor by their ID


@app.route("/api/doctors/<int:doctor_id>", methods=["GET"])
def get_doctor(doctor_id):

    doctor = next((doc for doc in doctors if doc["id"] == doctor_id), None)

    if doctor:
        return jsonify(doctor)

    else:
        return jsonify({"error": "No doctor could be found."}), 404


# Define a route to book an appointment with a doctor
@app.route("/api/appointments", methods=["POST"])
def book_appointment():
    data = request.get_json()
    doctor_id = data.get("doctor_id")
    slot = data.get("slot")

    try:
        doctor = next((doc for doc in doctors if doc["id"] == doctor_id), None)
        slot_availability = next((availability for availability in doctor["availability"] if availability["day"] == slot["day"] and availability["start_time"] <= slot["start_time"] and availability["end_time"] >= slot["end_time"]), None)
    except (KeyError, StopIteration):
        return jsonify({"error": "Invalid request body."}), 400

    if slot_availability:
        slot_availability["remaining_slots"] -= 1

        appointments.append({"doctor_id": doctor_id, "slot": slot})

        return jsonify({"message": "Appointment successfully scheduled"})
    else:
        return jsonify({"error": "There is no available slot for the specified day and time."}), 400



if __name__ == "__main__":

    # Start the Flask development server with debug mode enabled
    app.run(debug=True)
