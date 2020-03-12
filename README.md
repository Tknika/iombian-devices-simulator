# IoMBian Devices Simulator

Small auxiliary program that helps testing the '[IoMBian Discover](https://github.com/Tknika/iombian-discover)' tool, simulating many IoMBian devices.

## Usage

Clone the repository:

```bash
git clone https://github.com/Tknika/iombian-devices-simulator
```

Install the virtual environment and the dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a list of devices:

```python
nano src/people.py

people = [
    {"name": "...", "last_name": "..."},
    {"name": "...", "last_name": "..."},
    {"name": "...", "last_name": "..."},
    {"name": "...", "last_name": "..."}
}
```

Finally, launch the main application:

```
python src/main.py
```

## Author

(c) 2020 [Tknika](https://tknika.eus/) ([Aitor Iturrioz](https://github.com/bodiroga))

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
