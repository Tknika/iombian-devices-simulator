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
