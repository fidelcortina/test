import pathlib
d = pathlib.Path(__file__).parent
page = (d/'page.html').read_text().replace('/*STAGE_KIT*/', (d/'stage.js').read_text())
(d/'artifact.html').write_text(page)
(d.parent/'floor-preview.html').write_text('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n</head>\n<body>\n' + page + '\n</body>\n</html>\n')
