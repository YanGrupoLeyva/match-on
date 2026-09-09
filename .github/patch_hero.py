from pathlib import Path
import re
p=Path('index.html')
s=p.read_text(encoding='utf-8')
css='''.hero-mini-schema{width:min(1500px,100%);margin-top:30px;padding:13px 18px 16px;border-radius:24px;border:1px solid rgba(255,255,255,.08);background:linear-gradient(180deg,rgba(255,255,255,.025),rgba(0,140,255,.03));box-shadow:inset 0 1px 0 rgba(255,255,255,.04)}
.hero-mini-top{display:flex;justify-content:center;align-items:center;margin-bottom:7px}.hero-mini-bridge{width:1px;height:10px;margin:0 auto 7px;background:linear-gradient(rgba(0,229,255,0),rgba(0,229,255,.56),rgba(0,229,255,0))}
.hero-mini-flow{display:grid;grid-template-columns:minmax(130px,1fr) 24px minmax(150px,1fr) 24px minmax(150px,1fr) 24px minmax(150px,1fr) 24px minmax(180px,1.15fr);align-items:center;gap:8px}
.hero-mini-node{padding:11px 12px;border-radius:15px;border:1px solid rgba(255,255,255,.065);background:linear-gradient(180deg,rgba(8,20,33,.78),rgba(5,12,20,.92));color:#e5f5fb;font-size:11px;font-weight:700;letter-spacing:.18px;line-height:1.3;min-height:46px;display:flex;align-items:center;justify-content:center;text-align:center;box-shadow:inset 0 1px 0 rgba(255,255,255,.025)}
.hero-mini-core{padding:10px 18px;border-radius:15px;border:1px solid rgba(0,229,255,.22);background:radial-gradient(circle at 50% 0,rgba(0,229,255,.09),transparent 58%),linear-gradient(180deg,rgba(10,31,49,.92),rgba(5,12,20,.97));box-shadow:0 0 20px rgba(0,229,255,.04),inset 0 1px 0 rgba(255,255,255,.045);text-align:center;min-width:210px}.hero-mini-core strong{display:block;font-family:Oxanium,sans-serif;font-size:17px;letter-spacing:-.4px;line-height:1.05}.hero-mini-core span{display:block;margin-top:4px;color:#b9cfdb;font-size:10px;font-weight:600;letter-spacing:.15px;text-transform:uppercase}
.hero-mini-link{width:100%;height:1px;background:linear-gradient(90deg,rgba(0,229,255,0),rgba(0,229,255,.55),rgba(0,229,255,0))}'''
s=re.sub(r'\.hero-mini-schema\{.*?\.hero-mini-link\{.*?\}',css,s,count=1,flags=re.S)
markup='''<div class="hero-mini-schema">
        <div class="hero-mini-top"><div class="hero-mini-core"><strong>SPORTS-ON</strong><span>núcleo conectado</span></div></div>
        <div class="hero-mini-bridge"></div>
        <div class="hero-mini-flow">
          <div class="hero-mini-node">MÁQUINAS FÍSICAS</div><div class="hero-mini-link"></div>
          <div class="hero-mini-node">DASHBOARD OPERADORES</div><div class="hero-mini-link"></div>
          <div class="hero-mini-node">MÓDULO DE RECAUDACIÓN</div><div class="hero-mini-link"></div>
          <div class="hero-mini-node">MÓDULO DE COMPETICIÓN</div><div class="hero-mini-link"></div>
          <div class="hero-mini-node">APP JUGADORES / COMUNIDAD</div>
        </div>
      </div>
      <div class="hero-strip">'''
s=re.sub(r'<div class="hero-mini-schema">.*?<div class="hero-strip">',markup,s,count=1,flags=re.S)
s=s.replace('.hero-mini-schema{padding:14px 12px 14px;overflow-x:auto}.hero-mini-flow{grid-template-columns:130px 20px 145px 20px 160px 20px 145px 20px 145px 20px 175px;min-width:1180px;gap:6px}.hero-mini-node{font-size:10px;padding:10px 10px;min-height:42px}.hero-mini-core{padding:11px 12px}.hero-mini-core strong{font-size:16px}', '.hero-mini-schema{padding:14px 12px 14px;overflow-x:auto}.hero-mini-flow{grid-template-columns:130px 20px 145px 20px 145px 20px 145px 20px 175px;min-width:980px;gap:6px}.hero-mini-node{font-size:10px;padding:10px 10px;min-height:42px}.hero-mini-core{padding:10px 12px;min-width:190px}.hero-mini-core strong{font-size:16px}')
p.write_text(s,encoding='utf-8')
