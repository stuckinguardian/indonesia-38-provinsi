# Data Wilayah 38 Provinsi Indonesia (Indonesia Regions API)

This repository provides data and API for Indonesia's administrative regions, including Provinces (Provinsi), Regencies/Cities (Kabupaten/Kota), Districts (Kecamatan), and Villages (Kelurahan/Desa).

## 🇮🇩 Deskripsi (Description in Indonesian)

Data meliputi Provinsi, Kabupaten/Kota, Kecamatan, dan Kelurahan. Kode Penomoran wilayah berdasarkan format yang berlaku di Kementerian Dalam Negeri sebagai contoh berikut ini:

> - **31.74.06.1003** merupakan kode Wilayah Kelurahan Pondok Labu dengan format pemisahan dengan . (titik)
> - **31** merupakan Kode Provinsi DKI Jakarta
> - **31.74** merupakan Kode Kota Jakarta Selatan
> - **31.74.06** merupakan Kode Kecamatan Cilandak
> - **31.74.06.1003** merupakan Kode Kelurahan Pondok Labu

## 🌍 Description (in English)

This repository contains data for Indonesia's 38 provinces and their administrative subdivisions. The data follows the official coding format used by Indonesia's Ministry of Home Affairs (Kementerian Dalam Negeri), with hierarchical IDs representing each administrative level.

## 📁 Project Structure

```
wilayah-api/
├── data/
│   ├── raw/       # CSV data files
│   └── json/      # Generated JSON output files
├── tools/         # Python scripts
│   └── build.py   # Converts CSV to JSON
└── requirements.txt
```

## ⚙️ Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/indonesia-38-provinsi.git
   cd indonesia-38-provinsi
   ```

2. Set up a Python virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Converting CSV to JSON

Run the build script to convert CSV data to JSON format:

```
python tools/build.py
```

This will create a folder structure in `data/json/` containing:
- `provinsi.json` - All provinces
- `regencies/` - Regencies/cities for each province
- `districts/` - Districts for each regency
- `villages/` - Villages for each district

### JSON Data Format

The JSON data is structured as an array of objects with `id` and `name` properties:

```json
[
  {"id": "31", "name": "DKI JAKARTA"},
  {"id": "32", "name": "JAWA BARAT"},
  ...
]
```

### Hierarchical Data Access

The data follows a hierarchical structure where each administrative level is stored in separate files organized by their parent ID.

## 🌐 Deployment Options

There are several ways to deploy and use this data as an API:

### 1. Static File Hosting (Simplest)

Host the generated JSON files on any static file hosting service:

1. Run the build script to generate all JSON files
2. Upload the contents of the `data/json` directory to:
   - GitHub Pages
   - Netlify
   - Vercel
   - Amazon S3
   - Any web server (Nginx, Apache, etc.)

Example with GitHub Pages:
```bash
# After generating JSON files
git add data/json
git commit -m "Update JSON data"
git push origin main
# Enable GitHub Pages in your repository settings
```

### 2. Simple API Server

For more control, implement a minimal API server using Python:

1. Add the following to your requirements.txt:
```
pandas==2.*
flask==2.*
gunicorn==20.*  # For production deployment
```

2. Create an `app.py` file in the project root:
```python
from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

# Load JSON data
BASE_DIR = os.path.join(os.path.dirname(__file__), 'data', 'json')

@app.route('/api/provinsi', methods=['GET'])
def get_provinsi():
    with open(os.path.join(BASE_DIR, 'provinsi.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/api/regencies/<provinsi_id>', methods=['GET'])
def get_regencies(provinsi_id):
    file_path = os.path.join(BASE_DIR, 'regencies', f'{provinsi_id}.json')
    if not os.path.exists(file_path):
        return jsonify({"error": "Not found"}), 404
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/api/districts/<regency_id>', methods=['GET'])
def get_districts(regency_id):
    file_path = os.path.join(BASE_DIR, 'districts', f'{regency_id}.json')
    if not os.path.exists(file_path):
        return jsonify({"error": "Not found"}), 404
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/api/villages/<district_id>', methods=['GET'])
def get_villages(district_id):
    file_path = os.path.join(BASE_DIR, 'villages', f'{district_id}.json')
    if not os.path.exists(file_path):
        return jsonify({"error": "Not found"}), 404
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
```

3. Run locally:
```bash
python app.py
```

4. Deploy to a platform like Heroku, Railway, or Render:
```bash
# Example for Heroku
heroku create indonesia-wilayah-api
git push heroku main
```

### 3. Serverless Functions

Deploy as serverless functions on platforms like Vercel or Netlify:

1. Create a `/api` directory with serverless function files
2. Set up deployment configuration for your chosen platform

## 🔌 API Usage in Web Applications

### Fetch API (JavaScript)

```javascript
// Get all provinces
fetch('https://your-api-url.com/api/provinsi')
  .then(response => response.json())
  .then(provinces => {
    console.log(provinces);
    // Populate a dropdown with provinces
    const select = document.getElementById('provinceSelect');
    provinces.forEach(province => {
      const option = document.createElement('option');
      option.value = province.id;
      option.textContent = province.name;
      select.appendChild(option);
    });
  });

// Get regencies/cities for a selected province
function getRegencies(provinceId) {
  fetch(`https://your-api-url.com/api/regencies/${provinceId}`)
    .then(response => response.json())
    .then(regencies => {
      // Similar logic to populate regency dropdown
    });
}
```

### Axios (JavaScript)

```javascript
// Using Axios library
import axios from 'axios';

// Get all provinces
axios.get('https://your-api-url.com/api/provinsi')
  .then(response => {
    const provinces = response.data;
    // Process data
  });

// Get districts for a selected regency
function getDistricts(regencyId) {
  axios.get(`https://your-api-url.com/api/districts/${regencyId}`)
    .then(response => {
      const districts = response.data;
      // Process data
    });
}
```

### React Example

```jsx
import { useState, useEffect } from 'react';
import axios from 'axios';

function RegionSelector() {
  const [provinces, setProvinces] = useState([]);
  const [regencies, setRegencies] = useState([]);
  const [selectedProvince, setSelectedProvince] = useState('');
  const [selectedRegency, setSelectedRegency] = useState('');

  useEffect(() => {
    // Fetch provinces on component mount
    axios.get('https://your-api-url.com/api/provinsi')
      .then(response => setProvinces(response.data))
      .catch(error => console.error('Error fetching provinces:', error));
  }, []);

  useEffect(() => {
    // Fetch regencies when a province is selected
    if (selectedProvince) {
      axios.get(`https://your-api-url.com/api/regencies/${selectedProvince}`)
        .then(response => setRegencies(response.data))
        .catch(error => console.error('Error fetching regencies:', error));
    }
  }, [selectedProvince]);

  return (
    <div>
      <select
        value={selectedProvince}
        onChange={(e) => setSelectedProvince(e.target.value)}
      >
        <option value="">Select Province</option>
        {provinces.map(province => (
          <option key={province.id} value={province.id}>
            {province.name}
          </option>
        ))}
      </select>
      
      <select
        value={selectedRegency}
        onChange={(e) => setSelectedRegency(e.target.value)}
        disabled={!selectedProvince}
      >
        <option value="">Select Regency/City</option>
        {regencies.map(regency => (
          <option key={regency.id} value={regency.id}>
            {regency.name}
          </option>
        ))}
      </select>
    </div>
  );
}
```

## 📚 API Endpoints

When deploying with an API server as described above, the following endpoints will be available:

| Endpoint | Description |
|----------|-------------|
| `GET /api/provinsi` | Returns a list of all provinces |
| `GET /api/regencies/{provinsi_id}` | Returns cities/regencies in the specified province |
| `GET /api/districts/{regency_id}` | Returns districts in the specified regency/city |
| `GET /api/villages/{district_id}` | Returns villages in the specified district |

Each endpoint returns JSON data in this format:
```json
[
  {"id": "31", "name": "DKI JAKARTA"},
  {"id": "32", "name": "JAWA BARAT"},
  ...
]
```

## 📄 Data License

This dataset is provided for public use. Please refer to the original data source policies for any restrictions.

## 🤝 Contributing

Contributions to improve the data or code are welcome. Please feel free to submit a pull request or open an issue.

## 📚 References

- [Kementerian Dalam Negeri Republik Indonesia](https://www.kemendagri.go.id/)
