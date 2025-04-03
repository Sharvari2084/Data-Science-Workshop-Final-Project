from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# Load the trained model
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "linear.pkl")  # Ensure you have the trained model file

with open(file_path, "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None  # Default value

    if request.method == "POST":
        try:
            engine_size = float(request.form["engine_size"])
            cylinders = int(request.form["cylinders"])
            co2_emissions = float(request.form["co2_emissions"])

            # Predict using the model
            prediction = model.predict([[engine_size, cylinders, co2_emissions]])[0]

            return render_template("index.html", prediction=prediction)
        except Exception as e:
            prediction = f"Error: {e}"
            return render_template("index.html", prediction=prediction)
    
    return render_template("index.html", prediction=None)

if __name__ == "__main__":
    app.run(debug=True)
