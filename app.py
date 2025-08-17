from flask import Flask, redirect

app = Flask(__name__)

# Store scan count (reset if you restart server)
scan_count = 0
max_scans = 3

# Links
first_link = "https://docs.google.com/forms/d/1qp0k-40LqtyqxnCBcP3mJQjEMuDkdaRADHDqOym9qZw/edit?pli=1"
second_link = "https://docs.google.com/forms/d/1Hi79D7G8Ep-dyhP9MWU77bi2eEEMDmmBV_iAcgcfNwo/edit"

@app.route("/")
def scan():
    global scan_count
    scan_count += 1

    if scan_count <= max_scans:
        return redirect(first_link)
    else:
        return redirect(second_link)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
