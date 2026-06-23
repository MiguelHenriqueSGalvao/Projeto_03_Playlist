import streamlit as st

musicas = {
    "Dunamis Movement": {
        "Estações": "https://youtu.be/8JeWLB0992k?si=uZoMk6Z0udyNDvCf",
        "O nome dEle é Jesus": "https://youtu.be/Ntv10j6Sw1w?si=iX3nTe-WNTEP2fnO",
    },
    "Coldplay": {
        "Yellow": "https://youtu.be/yKNxeF4KMsY?si=BIc8vH1GL-_1lF-e",
        "Viva La Vida": "https://youtu.be/dvgZkm1xWPE?si=dxX9rxHViNJ2hHuq",
    },
    "Forrest Frank": {
        "YOUR WAY'S A BETTER": "https://youtu.be/T1LRsp8qBY0?si=Mg0fHlMrEsWlC1H4",
        "GOOD DAY": "https://youtu.be/Uc_HxKMKB_E?si=NIIqTD9ZItj_OybW"
    },
    "OneRepublic": {
        "I Lived": "https://youtu.be/z0rxydSolwU?si=DeHyI30N1PEsNukw",
        "Counting Stars": "https://youtu.be/hT_nvWreIhg?si=zwHvZ1vKIGyVz4bO"
    },
    "Elis Regina": {
        "Tiro ao Álvaro": "https://youtu.be/caEFyFRc91c?si=GQAcAygn37CElTPA",
        "O Bêbado e a Equilibrista": "https://youtu.be/oCcREJdgRXM?si=OhUTsguywI68lZXW"
    },
    "Felipe Rodrigues": {
        "Tudo é perda": "https://youtu.be/qxzQR5uwWsk?si=i7iyX2pzAEexn8fr",
        "SAUDADE": "https://youtu.be/23kl8jSXRok?si=OEVS4Y4_Ey3XAW3H"
    },
    "Josiah Queen": {
        "The Prodigal": "https://youtu.be/Hk0ZMKqJNWQ?si=mzddZ4scRXg6gETl",
        "Dusty Bibles": "https://youtu.be/IM2nMeXvor0?si=BX8BhGztM_4fs3U8"
    },
    "Avicii": {
        "The Nights": "https://youtu.be/UtF6Jej8yb4?si=5R98dgTcGcZRmyLo",
        "Waiting for Love": "https://youtu.be/cHHLHGNpCSA?si=w5FpM8OK7XGfYnxa"
    },
    "Elevation RHYTHM": {
        "Goodbye Yesterday": "https://youtu.be/qOD9M95_fS0?si=F0e-yrFLQ_NXV8_s",
        "Washed": "https://youtu.be/JjgkhHlTROQ?si=sUgFfbEOBq9Dr4EB"
    },
    "Caetano Veloso": {
        "Alegria, Alegria": "https://youtu.be/WL8l8olaMmI?si=3n-HzdUvO2ChzdcD",
        "Saudade": "https://youtu.be/j9UbE1slI-Q?si=qbFsZwQWwP6UGD2i"
    },
    "Marisa Monte": {
        "Ainda Bem": "https://youtu.be/Pmt01TGsGGA?si=bomu9b5MjgTBHFZc",
        "Velha Infância": "https://youtu.be/dQjO0zo12Go?si=Xf0DoxkO4CSTpaIW"
    },
    "Cássia Eller": {
        "O Segundo Sol": "https://youtu.be/eHHoheI5dK0?si=9TW-zCQTIk97LJjB",
        "Malandragem": "https://youtu.be/kjR_jfCHLQc?si=W_8KBkSc8upY5K8G"
    },
    "Tim Maia": {
        "Réu Confesso": "https://youtu.be/DET4QHe66c8?si=oiCLWDrs1JM_FSeH",
        "Acenda o Farol": "https://youtu.be/tPp9zkjfj7Q?si=XBNJx9DPNFk0lBHQ"
    },
    "FHOP Music": {
        "Colossenses e Suas Linhas De Amor": "https://youtu.be/MeX0yHMs9Nk?si=0aooryEHdHVnL5ZI",
        "Sublime": "https://youtu.be/7GWZwO0MdsY?si=0iZ_iAU0zHTiOCFS"
    },
}

st.sidebar.image("logo.png")
artista = st.sidebar.selectbox("Selecione o artista", musicas.keys())
musicas_artista = musicas[artista]

# st.title(artista)
# for musica in musicas_artista.items():
#     titulo, link = musica
#     st.subheader(titulo)
#     st.video(link)

st.title(artista)
video,sobre = st.tabs(['video','sobre'])

with video:
    for musica in musicas_artista.items():
        titulo, link = musica
        st.subheader(titulo)
        st.video(link)
with sobre:
    if artista == "Dunamis Moviment":
        st.markdown("""
# ✨ Dunamis Movement

> *Um movimento de despertar, transformação e avivamento.*

---

## 🌎 Sobre

O **Dunamis Movement** é um ministério cristão brasileiro que busca despertar uma geração para viver o sobrenatural de Deus no cotidiano. Seu propósito é formar discípulos apaixonados por Jesus e influenciar a sociedade através da fé.

---

## 🔥 Missão

- Proclamar o Evangelho.
- Equipar jovens e líderes.
- Desenvolver uma cultura de oração e adoração.
- Transformar vidas e nações através do amor de Cristo.

---

## 🎵 Música e Adoração

O movimento também é conhecido por suas canções e momentos de adoração que marcaram milhares de pessoas. As músicas expressam entrega, intimidade com Deus e paixão por Sua presença.

### Destaques

- **Tua Presença**
- **Santo Espírito**
- **Que Ele Cresça**
- **A Ele a Glória**

---

## 🤍 Valores

✨ Jesus no centro.

🤝 Comunhão e discipulado.

🔥 Avivamento e transformação.

🌎 Impactar a sociedade através do Reino de Deus.

---

<div style="text-align:center; padding:20px;">
<h3><i>"Uma geração apaixonada por Jesus e comprometida em transformar o mundo."</i></h3>
</div>
""", unsafe_allow_html=True)
    elif artista == "Coldplay":
        st.markdown("""
# 🌌 Coldplay

> *"Look at the stars, look how they shine for you..."*

---

## 🎶 Sobre

O **Coldplay** é uma banda britânica formada em Londres em 1997, conhecida por unir rock alternativo, pop e elementos eletrônicos em músicas que falam sobre amor, esperança, sonhos e humanidade.

Composta por **Chris Martin**, **Jonny Buckland**, **Guy Berryman** e **Will Champion**, a banda se tornou uma das mais influentes do século XXI.

---

## ✨ Álbuns Marcantes

### 💛 Parachutes (2000)
- Yellow
- Trouble
- Shiver

### 🌎 A Rush of Blood to the Head (2002)
- The Scientist
- Clocks
- In My Place

### 🎨 Viva la Vida or Death and All His Friends (2008)
- Viva La Vida
- Violet Hill
- Strawberry Swing

### 🌌 Mylo Xyloto (2011)
- Paradise
- Charlie Brown
- Every Teardrop Is a Waterfall

### ⭐ Music of the Spheres (2021)
- Higher Power
- My Universe
- Coloratura

---

## 💫 Estilo

- 🎹 Rock Alternativo
- 🌈 Pop Experimental
- 🎼 Música Atmosférica
- 🌍 Temas de Amor, Esperança e Unidade

---

## 🏆 Conquistas

- Diversos prêmios Grammy.
- Mais de 100 milhões de discos vendidos.
- Turnês mundiais históricas.
- Uma das bandas mais ouvidas do mundo.

---

## 🤍 Frases que marcaram

> "Lights will guide you home."

> "Nobody said it was easy."

> "You are a sky full of stars."

---

<div style="text-align:center; padding:30px;">
<h2>🌌✨ Coldplay ✨🌌</h2>
<p><i>Uma trilha sonora para sonhos, memórias e esperança.</i></p>
</div>
""", unsafe_allow_html=True)
    elif artista == "Forrest Frank":
        st.markdown("""
# ☀️ Forrest Frank

> *"Good Day, good God."*

---

## 🎶 Sobre

**Forrest Frank** é um cantor, compositor e produtor americano conhecido por combinar elementos de pop, hip-hop, lo-fi e música cristã contemporânea em um estilo leve, alegre e profundamente centrado em Jesus.

Anteriormente integrante do duo **Surfaces**, Forrest iniciou sua carreira solo com o propósito de criar músicas que transmitissem esperança, paz e a alegria encontrada em Deus.

---

## ✨ Estilo Musical

- ☀️ Pop Cristão
- 🎹 Lo-fi
- 🎧 Indie Pop
- 🌊 Influências de Hip-Hop e R&B
- 🙏 Letras inspiradas na fé e na gratidão

---

## 🎵 Canções em Destaque

### 🌞 GOOD DAY
Uma celebração da bondade de Deus em todos os momentos.

### 🤍 NEVER GET USED TO THIS
Canção sobre maravilhar-se constantemente com o amor e a graça do Senhor.

### ✨ UP!
Uma música alegre e contagiante sobre viver com esperança.

### 🌊 NO LONGER BOUND
Uma declaração de liberdade em Cristo.

### 🙌 YOUR WAY'S BETTER
Uma das músicas mais populares de Forrest Frank, lembrando que os caminhos de Deus são sempre melhores.

---

## 🌎 Mensagem

A música de Forrest Frank procura mostrar que seguir Jesus não significa viver sem alegria, mas experimentar uma vida cheia de propósito, gratidão e esperança.

---

## 💙 Valores

✝️ Jesus acima de tudo.

☀️ Alegria e gratidão.

🤝 Amor ao próximo.

🌎 Impactar pessoas através da música.

---

## 📖 Versículo que representa sua mensagem

> "A alegria do Senhor é a vossa força."
>
> **Neemias 8:10**

---

<div style="text-align:center; padding:30px;">
<h2>☀️ Forrest Frank ☀️</h2>
<p><i>Fé, alegria e boas vibrações para a glória de Deus.</i></p>
</div>
""", unsafe_allow_html=True)
    elif artista == "OneRepublic":
        st.markdown("""
# 🌎 OneRepublic

> *"Dreaming out loud, chasing something bigger."*

---

## 🎶 Sobre

**OneRepublic** é uma banda americana de pop rock formada em 2002, conhecida por suas melodias emocionantes, letras inspiradoras e uma sonoridade que mistura pop, rock e elementos eletrônicos.

Liderada pelo cantor e compositor **Ryan Tedder**, a banda conquistou fãs ao redor do mundo com músicas que falam sobre esperança, sonhos, amor, superação e as experiências da vida.

---

## ✨ Estilo Musical

- 🎸 Pop Rock
- 🎹 Alternative Pop
- 🎧 Música Eletrônica
- 🌎 Influências Folk e Indie
- 🎼 Canções emocionantes e cinematográficas

---

## 🎵 Canções em Destaque

### ✨ Counting Stars
Uma das músicas mais famosas da banda, sobre buscar algo maior do que riqueza material.

### 🌍 I Lived
Um hino sobre viver intensamente e aproveitar cada momento.

### 🌌 Secrets
Uma canção sobre autenticidade e vulnerabilidade.

### ❤️ Apologize
O sucesso que levou a banda ao reconhecimento mundial.

### 🌅 Good Life
Uma celebração das pequenas alegrias da vida.

### 🌠 Run
Uma música sobre seguir em frente, apesar das dificuldades.

---

## 🌎 Mensagem

As músicas do OneRepublic frequentemente exploram temas de esperança, perseverança e propósito, inspirando pessoas a viverem com intensidade e significado.

---

## 🏆 Conquistas

- Mais de 16 bilhões de reproduções em plataformas digitais.
- Diversos singles certificados em vários países.
- Turnês mundiais de grande sucesso.
- Uma das bandas pop-rock mais influentes do século XXI.

---

## 🤍 O que torna o OneRepublic especial?

✨ Letras profundas e inspiradoras.

🎹 Arranjos sofisticados e emocionantes.

🌎 Uma sonoridade que atravessa diferentes estilos.

🎼 Canções que se tornam trilhas sonoras de momentos marcantes.

---

## 💫 Frases que marcaram

> "Everything that kills me makes me feel alive."

> "Hope when you take that jump, you don't fear the fall."

> "I wish that I could witness all your joy and all your pain."

---

<div style="text-align:center; padding:30px;">
<h2>🌌 OneRepublic 🌌</h2>
<p><i>Músicas para sonhar, viver e lembrar.</i></p>
</div>
""", unsafe_allow_html=True)
    elif artista == "Elis Regina":
        st.markdown("""
# 🎙️ Elis Regina

> *"A emoção não tem época."*

---

## 🎶 Sobre

**Elis Regina** foi uma das maiores vozes da música brasileira. Nascida em Porto Alegre, em 1945, tornou-se um símbolo da MPB graças à sua interpretação intensa, técnica vocal extraordinária e presença de palco incomparável.

Sua capacidade de transmitir emoção transformava cada canção em uma experiência única, fazendo dela uma das artistas mais admiradas da história da música brasileira.

---

## ✨ Estilo Musical

- 🇧🇷 Música Popular Brasileira (MPB)
- 🎷 Samba-Jazz
- 🎹 Bossa Nova
- 🎺 Jazz Brasileiro
- 🎼 Canção Popular

---

## 🎵 Canções em Destaque

### 🚂 Como Nossos Pais
Uma reflexão poderosa sobre gerações, mudanças e permanências.

### 🌅 Águas de Março
Ao lado de Tom Jobim, criou uma das gravações mais icônicas da música brasileira.

### 🌻 Fascinação
Uma interpretação delicada e emocionante de um clássico atemporal.

### 🌎 O Bêbado e a Equilibrista
Tornou-se um símbolo de esperança durante a redemocratização do Brasil.

### 💙 Romaria
Uma homenagem sensível à fé e à cultura popular brasileira.

---

## 🌟 Legado

Elis Regina ajudou a revelar compositores que se tornariam gigantes da música brasileira, como:

- 🎼 Milton Nascimento
- 🎹 João Bosco
- ✍️ Aldir Blanc
- 🎸 Belchior
- 🎶 Ivan Lins

Sua influência continua presente em artistas de diferentes gerações.

---

## 🏆 Por que Elis Regina é única?

✨ Interpretação intensa e autêntica.

🎙️ Técnica vocal considerada uma das melhores do Brasil.

🇧🇷 Forte conexão com a cultura brasileira.

🎼 Capacidade de transformar letras em histórias vivas.

---

## 🤍 Frases que marcaram sua trajetória

> "A arte deve emocionar."

> "Cantar é contar histórias com a alma."

---

## 🌹 Uma Voz Eterna

Mais do que uma cantora, Elis Regina tornou-se um patrimônio cultural brasileiro. Sua música continua atravessando gerações, emocionando quem busca beleza, profundidade e verdade na arte.

---

<div style="text-align:center; padding:30px;">
<h2>🌹 Elis Regina 🌹</h2>
<p><i>A voz que transformou canções em emoções eternas.</i></p>
</div>
""", unsafe_allow_html=True)
    elif artista == "Felipe Rodrigues":
        st.markdown("""
# ✝️ Felipe Rodrigues

> *"Que Cristo cresça, e que nós apenas reflitamos Sua graça."*

---

## 🎶 Sobre

**Felipe Rodrigues** é um cantor e compositor cristão brasileiro conhecido por suas canções de adoração e por letras que apontam para Jesus com simplicidade e profundidade.

Seu ministério é marcado por músicas que convidam à intimidade com Deus, ao arrependimento e a uma vida centrada em Cristo.

---

## ✨ Estilo Musical

- 🎹 Adoração Contemporânea
- ✝️ Música Cristã
- 🎼 Worship
- 🤍 Canções de Intimidade
- 🙏 Louvor Congregacional

---

## 🎵 Canções em Destaque

### 🔥 Som da Chuva
Uma canção sobre sede pela presença de Deus e avivamento.

### 🙏 Vem Me Buscar
Um clamor por comunhão e dependência do Senhor.

### ✨ Jesus é Suficiente
Uma declaração de que Cristo é tudo o que precisamos.

### 🤍 Lugar Secreto
Um convite para encontrar Deus na intimidade.

---

## 🌎 Mensagem

As canções de Felipe Rodrigues têm como centro a pessoa de Jesus Cristo, enfatizando a graça, a santidade e a importância de uma vida guiada pelo Espírito Santo.

---

## 💙 Valores

✝️ Cristo acima de tudo.

🙏 Vida de oração.

🤝 Serviço e comunhão.

🔥 Paixão pela presença de Deus.

📖 Fidelidade às Escrituras.

---

## 📖 Versículo

> "Importa que Ele cresça e que eu diminua."
>
> **João 3:30**

---

## 🌟 Legado

Mais do que produzir músicas, Felipe Rodrigues busca formar uma geração apaixonada por Jesus, comprometida em viver o Evangelho de maneira autêntica e transformadora.

---

<div style="text-align:center; padding:30px;">
<h2>✝️ Felipe Rodrigues ✝️</h2>
<p><i>Canções para quem deseja conhecer mais profundamente a Cristo.</i></p>
</div>
""", unsafe_allow_html=True)
    elif artista == "Josiah Queen":
        st.markdown("""
# 🌿 Josiah Queen

> *"I don't wanna miss what Heaven is doing."*

---

## 🎶 Sobre

**Josiah Queen** é um cantor e compositor cristão americano que ganhou destaque por suas músicas sinceras, acústicas e profundamente centradas em Jesus.

Conhecido por letras simples, mas cheias de significado, Josiah tem alcançado uma nova geração através de canções que falam sobre devoção, graça e o desejo de viver mais próximo de Deus.

---

## ✨ Estilo Musical

- 🌿 Indie Folk
- 🎸 Acoustic Worship
- ✝️ Música Cristã Contemporânea
- 🤍 Louvor Intimista
- 🎼 Singer-Songwriter

---

## 🎵 Canções em Destaque

### 👑 The Prodigal
Uma reflexão sobre a graça e o amor do Pai, inspirada na parábola do filho pródigo.

### 🌊 I Am Barabbas
Uma poderosa lembrança da redenção oferecida por Cristo.

### ❤️ My Promised Land
Uma canção sobre confiar nas promessas de Deus em meio às dificuldades.

### ✨ Fishes and Loaves
Uma declaração de dependência e confiança na provisão do Senhor.

### 🌿 Garden in Manhattan
Uma música que fala sobre encontrar Deus em meio ao cotidiano.

---

## 🌎 Mensagem

As músicas de Josiah Queen apontam para uma fé simples e genuína, convidando as pessoas a caminharem com Jesus não apenas nos grandes momentos, mas também na vida comum.

---

## 💙 Valores

✝️ Jesus acima de tudo.

📖 Fidelidade à Palavra.

🙏 Vida de devoção e oração.

🤍 Simplicidade e autenticidade.

🌎 Levar esperança através da música.

---

## 📖 Versículo

> "Buscai, pois, em primeiro lugar, o Reino de Deus e a sua justiça."
>
> **Mateus 6:33**

---

## 🌟 O que torna Josiah Queen especial?

✨ Letras profundamente pessoais.

🌿 Sonoridade acústica e acolhedora.

🙏 Músicas que inspiram uma caminhada mais íntima com Deus.

🤍 Uma mensagem simples, mas poderosa: Jesus é suficiente.

---

<div style="text-align:center; padding:30px;">
<h2>🌿 Josiah Queen 🌿</h2>
<p><i>Canções para uma geração que deseja conhecer Jesus de forma simples e verdadeira.</i></p>
</div>
""", unsafe_allow_html=True)
    elif artista == "Avicii":
        st.markdown("""
# ◢ ◤ Avicii

> *"One day you'll leave this world behind, so live a life you will remember."*

---

## 🎶 Sobre

**Avicii**, nome artístico de **Tim Bergling**, foi um DJ, produtor e compositor sueco que revolucionou a música eletrônica ao unir EDM, pop, folk e elementos acústicos em canções que marcaram uma geração.

Sua música transcendeu pistas de dança, tornando-se trilha sonora para sonhos, viagens, amizades e memórias inesquecíveis.

---

## ✨ Estilo Musical

- 🎧 EDM
- 🌎 Progressive House
- 🎸 Folk Eletrônico
- 🎹 Dance Pop
- 🌌 Música Atmosférica

---

## 🎵 Canções em Destaque

### 🌄 Wake Me Up
Uma mistura inovadora entre música eletrônica e folk, tornando-se um dos maiores sucessos da década.

### ⭐ The Nights
Um hino sobre viver intensamente e criar memórias inesquecíveis.

### 🌊 Waiting For Love
Uma canção sobre esperança e perseverança.

### ❤️ Hey Brother
Uma homenagem aos laços familiares e à amizade.

### 🌌 Levels
Considerada uma das músicas mais influentes da história da EDM.

### 🌍 Without You
Uma poderosa colaboração com Sandro Cavazza.

---

## 🏆 Legado

- 🌎 Mais de bilhões de reproduções em plataformas digitais.
- 🎧 Um dos artistas mais influentes da música eletrônica.
- ✨ Responsável por aproximar o público pop da EDM.
- 🎼 Inspiração para uma nova geração de produtores musicais.

---

## 🤍 O que tornava Avicii especial?

✨ Melodias emocionantes.

🌌 Músicas que transmitiam liberdade e esperança.

🎸 A fusão única entre instrumentos acústicos e eletrônicos.

🎧 Uma sonoridade capaz de emocionar tanto quanto fazer dançar.

---

## 💫 Frases que marcaram

> "Live a life you will remember."

> "When thunder clouds start pouring down, light a fire they can't put out."

> "One day you'll leave this world behind."

---

## ♾️ Um Legado Eterno

Mesmo após sua partida, a música de Avicii continua inspirando milhões de pessoas ao redor do mundo. Seu legado permanece vivo em cada melodia, lembrando-nos da beleza da vida, da amizade e da importância de aproveitar cada momento.

---

<div style="text-align:center; padding:30px;">
<h2>◢ ◤ Avicii ◢ ◤</h2>
<p><i>Melodias para sonhar, viver e lembrar.</i></p>
</div>
""", unsafe_allow_html=True)
    elif artista == "Elevation RHYTHM":
        st.markdown("""
# ⚡ Elevation RHYTHM

> *"This is the sound of a generation running after Jesus."*

---

## 🎶 Sobre

**Elevation RHYTHM** é o ministério de jovens da **Elevation Church**, criado para alcançar uma nova geração com músicas vibrantes, autênticas e centradas em Jesus.

Com uma sonoridade que mistura pop, eletrônico e worship contemporâneo, o grupo se tornou uma das maiores referências da música cristã para jovens ao redor do mundo.

---

## ✨ Estilo Musical

- ⚡ Pop Worship
- 🎧 Música Eletrônica
- 🎹 Contemporary Christian Music
- 🌎 Pop Alternativo
- 🙌 Louvor Contemporâneo

---

## 🎵 Canções em Destaque

### 🌊 GOODBYE YESTERDAY
Uma declaração de liberdade e nova vida em Cristo.

### ☀️ THIS IS THE GOSPEL
Uma celebração da esperança encontrada em Jesus.

### ✨ WALK ON WATER
Uma música sobre confiar em Deus mesmo em meio às incertezas.

### 🌎 NEVER WALK AWAY
Uma lembrança da fidelidade de Deus em todos os momentos.

### ❤️ QUIET
Uma canção sobre encontrar paz na presença do Senhor.

### 🔥 OVER & OVER
Uma expressão da graça e do amor inesgotável de Deus.

---

## 🌎 Mensagem

As músicas do Elevation RHYTHM procuram comunicar o Evangelho de forma relevante para a nova geração, mostrando que seguir Jesus é viver uma vida cheia de propósito, alegria e esperança.

---

## 💙 Valores

✝️ Jesus acima de tudo.

🔥 Uma fé viva e autêntica.

🤝 Comunidade e discipulado.

🌎 Alcançar uma geração com o Evangelho.

🎶 Criatividade para a glória de Deus.

---

## 📖 Versículo

> "Ninguém despreze a tua mocidade; pelo contrário, torna-te padrão dos fiéis."
>
> **1 Timóteo 4:12**

---

## 🌟 O que torna o Elevation RHYTHM especial?

✨ Letras simples e profundas.

⚡ Uma sonoridade moderna e contagiante.

🙌 Canções para adoração e celebração.

🌎 Uma mensagem de esperança para a nova geração.

---

## 🤍 Frases que marcaram

> "Goodbye yesterday, I'm living in the light."

> "Over and over, Your mercy never ends."

> "This is the Gospel, this is our hope."

---

<div style="text-align:center; padding:30px;">
<h2>⚡ Elevation RHYTHM ⚡</h2>
<p><i>Uma geração apaixonada por Jesus, vivendo o ritmo da graça.</i></p>
</div>
""", unsafe_allow_html=True)
    elif artista == "Caetano Veloso":
        st.markdown("""
# 🌿 Caetano Veloso

> *"Gente é pra brilhar, não pra morrer de fome."*

---

## 🎶 Sobre

**Caetano Veloso** é um dos maiores nomes da música brasileira. Cantor, compositor, escritor e pensador, tornou-se uma figura central do movimento **Tropicália**, ajudando a reinventar a MPB ao unir tradição e inovação.

Com uma obra que atravessa décadas, Caetano construiu uma trajetória marcada pela poesia, pela liberdade artística e por uma profunda reflexão sobre o Brasil e a condição humana.

---

## ✨ Estilo Musical

- 🇧🇷 Música Popular Brasileira (MPB)
- 🌴 Tropicália
- 🎸 Folk
- 🎹 Bossa Nova
- 🎼 Samba e Música Experimental

---

## 🎵 Canções em Destaque

### 🌙 Sozinho
Uma das interpretações mais emocionantes da música brasileira.

### 🌿 O Leãozinho
Uma declaração de afeto simples e luminosa.

### 🌎 Terra
Composta durante o exílio, é uma das obras mais profundas de sua carreira.

### ☀️ Alegria, Alegria
Símbolo da Tropicália e da liberdade criativa.

### 💙 Você é Linda
Uma canção delicada sobre beleza e admiração.

### 🌊 Sampa
Uma homenagem poética à cidade de São Paulo.

---

## 🌟 Legado

Caetano Veloso é considerado um dos artistas mais influentes da cultura brasileira, tendo inspirado gerações de músicos e escritores com sua sensibilidade e ousadia artística.

Ao lado de nomes como:

- 🎙️ Gilberto Gil
- 🌹 Gal Costa
- 🎼 Tom Zé
- 🎹 Maria Bethânia

ajudou a moldar a identidade da música brasileira contemporânea.

---

## 🤍 O que torna Caetano único?

✨ Letras filosóficas e poéticas.

🌎 Um olhar profundo sobre o Brasil e o mundo.

🎼 Capacidade de transitar entre diferentes estilos musicais.

📖 Uma obra rica em referências culturais e literárias.

---

## 💫 Frases que marcaram

> "Narciso acha feio o que não é espelho."

> "Alguma coisa acontece no meu coração."

> "Gente é pra brilhar, não pra morrer de fome."

---

## 🌌 Uma Voz para o Tempo

Mais do que um cantor, Caetano Veloso é um cronista da alma brasileira. Sua música mistura memória, amor, filosofia e beleza, criando canções que permanecem vivas através das gerações.

---

<div style="text-align:center; padding:30px;">
<h2>🌿 Caetano Veloso 🌿</h2>
<p><i>Entre poesia e canção, uma das vozes mais singulares do Brasil.</i></p>
</div>
""", unsafe_allow_html=True)
    elif artista == "Marisa Monte":
        st.markdown("""
# 🌹 Marisa Monte

> *"Ainda bem que agora encontrei você..."*

---

## 🎶 Sobre

**Marisa Monte** é uma das artistas mais sofisticadas e influentes da música brasileira. Dona de uma voz delicada e inconfundível, construiu uma carreira marcada pela elegância, pela diversidade musical e pela busca constante pela excelência artística.

Ao longo das décadas, tornou-se referência da MPB contemporânea, transitando entre o samba, o pop, a bossa nova e a música experimental.

---

## ✨ Estilo Musical

- 🇧🇷 Música Popular Brasileira (MPB)
- 🌊 Samba
- 🎹 Bossa Nova
- 🎸 Pop Brasileiro
- 🎼 Música Alternativa

---

## 🎵 Canções em Destaque

### 🌹 Ainda Bem
Uma celebração do amor e da gratidão.

### ☀️ Beija Eu
Uma das músicas mais marcantes da MPB moderna.

### 🌙 Amor I Love You
Uma delicada combinação de poesia e romance.

### 🌿 Vilarejo
Uma canção sobre simplicidade, paz e felicidade.

### 🌊 Infinito Particular
Uma viagem íntima e poética.

### ✨ Depois
Uma reflexão sensível sobre o amor e o tempo.

---

## 🌟 Legado

Marisa Monte ajudou a renovar a música brasileira e foi integrante dos **Tribalistas**, ao lado de:

- 🎸 Arnaldo Antunes
- 🎹 Carlinhos Brown

Sua obra é admirada pela riqueza dos arranjos e pela profundidade das letras.

---

## 🤍 O que torna Marisa Monte única?

✨ Sofisticação e delicadeza.

🌎 Mistura harmoniosa entre tradição e modernidade.

🎼 Arranjos refinados e atemporais.

📖 Letras poéticas e cheias de sensibilidade.

---

## 💫 Frases que marcaram

> "Ainda bem que agora encontrei você."

> "É impossível ser feliz sozinho."

> "Há um vilarejo ali onde areja um vento bom."

---

## 🌌 Uma Voz de Delicadeza

Mais do que uma cantora, Marisa Monte é uma artista que transforma sentimentos em música. Sua obra é um convite à contemplação, ao amor e à beleza das pequenas coisas da vida.

---

<div style="text-align:center; padding:30px;">
<h2>🌹 Marisa Monte 🌹</h2>
<p><i>Elegância, poesia e a beleza da música brasileira.</i></p>
</div>
""", unsafe_allow_html=True)
    elif artista == "Cássia Eller":
        st.markdown("""
# 🎸 Cássia Eller

> *"O acaso vai me proteger enquanto eu andar distraído."*

---

## 🎶 Sobre

**Cássia Eller** foi uma das vozes mais intensas e autênticas da música brasileira. Com sua interpretação apaixonada e presença de palco marcante, tornou-se um ícone do rock nacional e da MPB.

Sua carreira foi caracterizada pela liberdade artística e pela capacidade de transformar cada canção em uma experiência profundamente humana e emocionante.

---

## ✨ Estilo Musical

- 🎸 Rock Brasileiro
- 🇧🇷 Música Popular Brasileira (MPB)
- 🎹 Blues
- 🌊 Samba
- 🎼 Folk e Música Alternativa

---

## 🎵 Canções em Destaque

### 🌻 Malandragem
Um dos maiores clássicos da música brasileira dos anos 90.

### ☀️ Segundo Sol
Uma interpretação inesquecível da canção de Nando Reis.

### 🌎 O Segundo Sol
Uma reflexão sobre esperança e transformação.

### 🌿 Palavras ao Vento
Uma canção sobre amor, despedidas e recomeços.

### 🌙 All Star
Uma das mais belas parcerias entre Cássia Eller e Nando Reis.

### 💙 Por Enquanto
Uma interpretação emocionante do clássico da Legião Urbana.

---

## 🌟 Legado

Cássia Eller marcou uma geração com sua autenticidade e sua capacidade de transitar entre diversos estilos musicais.

Ao longo de sua trajetória, interpretou canções de grandes nomes como:

- 🎸 Nando Reis
- 🕊️ Renato Russo
- 🌹 Cazuza
- 🎼 Chico Buarque
- 🎹 Djavan

---

## 🤍 O que torna Cássia Eller única?

✨ Uma voz poderosa e inconfundível.

🎸 Interpretações intensas e emocionantes.

🌎 Liberdade artística e autenticidade.

🎼 Capacidade de unir rock, MPB e blues com naturalidade.

---

## 💫 Frases que marcaram

> "O acaso vai me proteger enquanto eu andar distraído."

> "Quando o segundo sol chegar."

> "Estranho seria se eu não me apaixonasse por você."

---

## 🌌 Uma Voz Inesquecível

Mais do que uma cantora, Cássia Eller foi uma intérprete extraordinária. Sua música continua viva, emocionando diferentes gerações com a mesma intensidade, sinceridade e liberdade que marcaram sua trajetória.

---

<div style="text-align:center; padding:30px;">
<h2>🎸 Cássia Eller 🎸</h2>
<p><i>Intensidade, liberdade e uma das vozes mais marcantes da música brasileira.</i></p>
</div>
""", unsafe_allow_html=True)
    elif artista == "Tim Maia":
        st.markdown("""
# 👑 Tim Maia

> *"Não quero dinheiro, eu só quero amar."*

---

## 🎶 Sobre

**Tim Maia** foi um dos artistas mais carismáticos, talentosos e influentes da música brasileira. Dono de uma voz poderosa e de uma personalidade inconfundível, revolucionou a música nacional ao incorporar elementos do soul, funk, disco e da MPB.

Sua obra é marcada por canções apaixonadas, cheias de energia e autenticidade, que continuam atravessando gerações.

---

## ✨ Estilo Musical

- 🎷 Soul Brasileiro
- 🎸 Funk
- 🇧🇷 Música Popular Brasileira (MPB)
- 🎹 Disco Music
- 🎼 R&B

---

## 🎵 Canções em Destaque

### ❤️ Não Quero Dinheiro (Só Quero Amar)
Um dos maiores hinos da música brasileira.

### ☀️ Primavera
Uma canção repleta de esperança e romantismo.

### 🌎 Gostava Tanto de Você
Uma interpretação emocionante sobre saudade e amor.

### 🌙 Azul da Cor do Mar
Um clássico sobre sonhos e perseverança.

### ✨ Descobridor dos Sete Mares
Uma celebração da liberdade e da aventura.

### 🌿 Você
Uma das mais belas canções românticas de seu repertório.

---

## 🌟 Legado

Conhecido como o **Pai do Soul Brasileiro**, Tim Maia ajudou a popularizar ritmos internacionais no Brasil e influenciou inúmeros artistas.

Sua música abriu caminhos para nomes como:

- 🎸 Jorge Ben Jor
- 🎤 Sandra de Sá
- 🎹 Seu Jorge
- 🎼 Ed Motta
- 🎷 Cassiano

---

## 🤍 O que torna Tim Maia único?

✨ Uma voz poderosa e inconfundível.

🎶 Groove e musicalidade extraordinários.

🌎 Mistura perfeita entre soul, funk e MPB.

🎼 Canções que unem alegria, romantismo e emoção.

---

## 💫 Frases que marcaram

> "Não quero dinheiro, eu só quero amar."

> "Porque é primavera, te amo."

> "Ah! Se o mundo inteiro me pudesse ouvir."

---

## 🌌 Um Símbolo da Música Brasileira

Mais do que um cantor, Tim Maia foi uma força da natureza. Seu legado permanece vivo em cada acorde, em cada groove e em cada refrão que continua embalando histórias, amores e memórias.

---

<div style="text-align:center; padding:30px;">
<h2>👑 Tim Maia 👑</h2>
<p><i>O rei do soul brasileiro, onde emoção e ritmo caminham juntos.</i></p>
</div>
""", unsafe_allow_html=True)
    elif artista == "FHOP Music":
        st.markdown("""
# 🔥 FHOP Music

> *"Jesus é digno de tudo."*

---

## 🎶 Sobre

**FHOP Music** é o ministério de louvor da **Florianópolis House of Prayer (FHOP)**, uma comunidade cristã brasileira dedicada à adoração, intercessão e ao conhecimento de Deus.

Suas canções nascem de uma cultura de oração e têm impactado milhares de pessoas, convidando uma geração a viver uma vida centrada em Jesus e marcada pela presença de Deus.

---

## ✨ Estilo Musical

- 🙏 Worship
- 🎹 Adoração Contemporânea
- 🌊 Louvor Intimista
- 🎼 Música Cristã
- 🔥 Canções de Oração e Devoção

---

## 🎵 Canções em Destaque

### ❤️ Yeshua
Uma poderosa declaração de amor e adoração ao nome de Jesus.

### 🔥 Não Há Outro Lugar
Um convite para permanecer na presença de Deus.

### ✨ Ele Vem
Uma canção sobre esperança e a expectativa da volta de Cristo.

### 🌿 Tu És Tudo Que Eu Quero
Uma expressão de devoção e dependência do Senhor.

### ☀️ Santo Pra Sempre
Uma celebração da santidade e majestade de Deus.

### 👑 Maranata
Uma oração pela volta do Rei.

---

## 🌎 Mensagem

As músicas da FHOP nascem do desejo de formar uma geração apaixonada por Jesus, comprometida com a oração e com uma vida de intimidade com Deus.

---

## 💙 Valores

✝️ Jesus acima de tudo.

🔥 Vida de oração e intercessão.

📖 Fidelidade às Escrituras.

🤍 Adoração como estilo de vida.

🌎 Preparar uma geração para a volta de Cristo.

---

## 📖 Versículo

> "Uma coisa peço ao Senhor, e a buscarei: que eu possa morar na Casa do Senhor todos os dias da minha vida."
>
> **Salmos 27:4**

---

## 🌟 O que torna a FHOP especial?

✨ Canções nascidas na sala de oração.

🔥 Uma cultura de intimidade com Deus.

🎼 Louvores profundos e centrados em Cristo.

🤍 O desejo de ver Jesus conhecido e amado.

---

## 💫 Frases que marcam sua mensagem

> "Jesus é digno."

> "Não há outro lugar onde eu queira estar."

> "Maranata! Ora vem, Senhor Jesus."

---

## 🌌 Uma Casa de Oração

Mais do que um ministério de música, a **FHOP** é uma comunidade que busca cultivar dia e noite uma cultura de adoração, intercessão e amor por Jesus, inspirando uma geração a viver para aquilo que é eterno.

---

<div style="text-align:center; padding:30px;">
<h2>🔥 FHOP Music 🔥</h2>
<p><i>Canções nascidas na oração, para uma geração apaixonada por Jesus.</i></p>
</div>
""", unsafe_allow_html=True)