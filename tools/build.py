import pandas as pd, pathlib, json

ROOT = pathlib.Path(__file__).parent.parent
SRC  = ROOT / "data" / "raw"
OUT  = ROOT / "data" / "json"
OUT.mkdir(parents=True, exist_ok=True)

prov = pd.read_csv(SRC/"provinsi.csv", names=["id","name"])
reg  = pd.read_csv(SRC/"kabupaten_kota.csv", names=["id","name"])
kec  = pd.read_csv(SRC/"kecamatan.csv", names=["id","name"])
des  = pd.read_csv(SRC/"kelurahan.csv", names=["id","name"])

def dump(df, path):
    path.write_bytes(
        df.to_json(orient="records", force_ascii=False).encode("utf-8")
    )
dump(prov, OUT/"provinsi.json")

for pid in prov.id:
    parent = OUT / "regencies"
    parent.mkdir(exist_ok=True)
    dump(reg[reg.id.str.startswith(f"{pid}.")], parent/f"{pid}.json")

for rid in reg.id:
    parent = OUT / "districts"
    parent.mkdir(exist_ok=True)
    dump(kec[kec.id.str.startswith(f"{rid}.")], parent/f"{rid}.json")

for kid in kec.id:
    parent = OUT / "villages"
    parent.mkdir(exist_ok=True)
    dump(des[des.id.str.startswith(f"{kid}.")], parent/f"{kid}.json")
