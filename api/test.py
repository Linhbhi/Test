from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/long_task')
def long_task():
    time.sleep(15)  # Giả lập một tác vụ mất 15 giây
    return jsonify({"message": "Tác vụ đã hoàn thành!"})

if __name__ == '__main__':
    app.run(debug=True)
  
