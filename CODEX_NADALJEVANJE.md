# CODEX NADALJEVANJE - ELUCY design konfigurator

Ta datoteka je namenjena temu, da lahko projekt nadaljujes na drugem racunalniku,
tudi ce zgodovina pogovora v Codex/ChatGPT ni vidna.

## Kaj je projekt

Gre za osnovno spletno stran in konfigurator majic za ELUCY design.
Glavni poudarek je konfigurator, kjer uporabnik lahko:

- vidi 3D majico,
- vrti 3D model,
- nalozi bitno sliko,
- doda SVG,
- doda tekst,
- premika grafike po majici,
- spreminja velikost in rotacijo,
- zrcali grafiko,
- izbere barvo majice,
- doda vec grafik na isto majico,
- izbrise posamezno grafiko.

## Glavne datoteke

- `index.html` - osnovna vstopna stran.
- `konfigurator.html` - glavni konfigurator majic.
- `assets/models/tshirt/T_shirt_gltf.zip.gltf` - 3D model majice.
- `assets/models/tshirt/T_shirt_gltf.zip.bin` - binarna datoteka 3D modela.
- `assets/designs/be_the.svg` - prednalozen SVG dizajn.
- `assets/designs/chross.svg` - prednalozen SVG dizajn.
- `assets/designs/heart.svg` - prednalozen SVG dizajn.
- `preview-server.py` - lokalni server za testiranje.
- `start-preview.bat` - Windows zagon lokalnega serverja.

## Kaj naloziti na GitHub

Na GitHub nalozi VSEBINO mape `outputs`, ne zunanje projektne mape.

V root GitHub repozitorija morajo biti:

- `index.html`
- `konfigurator.html`
- `assets`
- `preview-server.py`
- `start-preview.bat`
- `README.md`
- `CODEX_NADALJEVANJE.md`

Mapa `assets` mora vsebovati:

- `assets/models/tshirt/T_shirt_gltf.zip.gltf`
- `assets/models/tshirt/T_shirt_gltf.zip.bin`
- `assets/designs/be_the.svg`
- `assets/designs/chross.svg`
- `assets/designs/heart.svg`

## GitHub Pages

Repository mora biti Public, ce uporabljas brezplacni GitHub Pages.

Nastavitve:

- Settings
- Pages
- Deploy from a branch
- Branch: `main`
- Folder: `/root`

Po nekaj minutah GitHub prikaze URL strani.

## Pomembna opomba o zgodovini pogovora

Zgodovina pogovora iz tega racunalnika se morda ne prikaze na sluzbenem
racunalniku, posebej ce uporabljas drug racun ali drug produkt
(ChatGPT spletni app, Codex app, drug workspace).

Zato naj Codex v sluzbi najprej prebere to datoteko:

`CODEX_NADALJEVANJE.md`

Predlagan prvi prompt v sluzbi:

> Nadaljuj projekt ELUCY design konfigurator. Najprej preberi `CODEX_NADALJEVANJE.md`, nato preglej `konfigurator.html` in mi povej, kaj razumes o trenutnem stanju.

## Trenutne funkcije konfiguratorja

### 3D model

Konfigurator uporablja Three.js in GLTF model majice.
Model se nalozi iz:

`assets/models/tshirt/T_shirt_gltf.zip.gltf`

Pomembno: stran mora biti odprta prek serverja ali GitHub Pages.
Ce se odpira direktno kot `file://`, lahko brskalnik blokira GLTF ali module.

### Grafike

Grafike se na majico lepijo kot DecalGeometry.
To pomeni:

- grafika sledi povrsini majice,
- ob vrtenju majice ostane na majici,
- med premikanjem se decal posodablja redkeje zaradi hitrosti,
- ob spustu miske se izrise koncna postavitev.

### SVG

SVG se ne more ohraniti kot pravi vektor na 3D povrsini.
Za 3D prikaz se pretvori v teksturo.
Trenutno SVG uporablja visjo teksturo za ostrejsi prikaz.

Prednalozeni SVG dizajni so v:

`assets/designs/`

### Bitne slike

Pri nalaganju bitnih slik obstaja opcija:

`Odstrani belo ozadje`

Pri JPG/JPEG se ta opcija privzeto izklopi, ker so JPG datoteke pogosto fotografije.
Pri logotipih jo lahko uporabnik rocno vklopi.

### Tekst

Tekst ima:

- izbor pisave,
- izbor barve,
- poljubno povecavo,
- tesnejsi oblikovalni okvir kot navadne slike.

## Znane tehnicne odlocitve

- Barve majic so premaknjene v levi panel ob 3D pogledu.
- Desni panel vsebuje knjiznico dizajnov, upload slike/SVG, tekst, seznam grafik in transformacije.
- Crtkani oblikovalni okvir se skrije, ko kliknes izven grafike.
- Ob kliku na grafiko se okvir spet pokaze.
- Obvestilno okence 3D statusa je skrito.
- Oznaka v 3D pogledu se imenuje `3D Pogled`.

## Kaj je treba se urediti kasneje

- Dodati pravi login ali PIN, ce bo javna testna stran na GitHub Pages.
- Preveriti delovanje na mobilnem telefonu.
- Dodati opozorila za prevelik tisk ali slabo resolucijo slike.
- Urediti bolj profesionalno zbirko prednalozenih dizajnov.
- Kasneje razmisliti o backendu za AI/CDR/EPS/PDF pretvorbe.

## Ce kaj ne deluje na GitHub Pages

Najprej preveri:

- ali so datoteke res v root repozitorija,
- ali je `index.html` v rootu,
- ali obstaja `konfigurator.html`,
- ali obstaja mapa `assets`,
- ali so 3D model datoteke v `assets/models/tshirt/`,
- ali so SVG dizajni v `assets/designs/`,
- ali poti v `konfigurator.html` niso absolutne Windows poti.

GitHub Pages ne zna brati lokalnih poti kot `D:\Grafike`.
Vse mora biti v repozitoriju.
