from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        as_number = request.form.get('as_number')
        prefix_type = request.form.get('prefix_type')
        prefix_length = request.form.get('prefix_length')

        if not name or not as_number or not prefix_type:
            error = "Missing required fields"
            return render_template('result.html', error=error)

        if prefix_length and not prefix_length.isdigit():
            error = "Prefix length must be a numeric value"
            return render_template('result.html', error=error)

        if prefix_type == 'ipv4':
            cmd = f'bgpq4 -AJEl {name} {as_number} -R'
        elif prefix_type == 'ipv6':
            cmd = f'bgpq4 -6AJEl {name} {as_number} -R'
        if prefix_length:
            cmd += f' {prefix_length}'
        cmd += ' -M "protocol bgp"'

        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                error = f"Command '{cmd}' failed with error: {result.stderr}"
                return render_template('result.html', error=error)

            output = result.stdout
            return render_template('result.html', name=name, output=output)
        except subprocess.CalledProcessError as e:
            error = f"Error executing command: {e}"
            return render_template('result.html', error=error)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
