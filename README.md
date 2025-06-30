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

## 📄 Data License

This dataset is provided for public use. Please refer to the original data source policies for any restrictions.

## 🤝 Contributing

Contributions to improve the data or code are welcome. Please feel free to submit a pull request or open an issue.

## 📚 References

- [Kementerian Dalam Negeri Republik Indonesia](https://www.kemendagri.go.id/)
