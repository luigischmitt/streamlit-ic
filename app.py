import streamlit as st

st.set_page_config(page_title="Futuro das Linguagens de Programação", page_icon="💻", layout="wide")

st.markdown("""
    <style>
    .main {
        background-color: #1e1e1e;
        padding: 10px;
        display: flex;
        flex-direction: column;
        min-height: 110vh; /* Ajusta a altura mínima para 100% da altura da tela */
        justify-content: center; /* Centraliza verticalmente */
    }
    .stTitle {
        font-family: 'Segoe UI', sans-serif;
        color: #f0f0f0;
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    .stSubheader {
        font-family: 'Segoe UI', sans-serif;
        color: #f0f0f0;
        font-size: 28px;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 20px;
    }
    .stMarkdown {
        font-family: 'Segoe UI', sans-serif;
        color: #d3d3d3;
        font-size: 18px;
        line-height: 1.6;
        text-align: justify;
        margin: 0 10px;
        margin-bottom: 40px; /* Aumenta a margem inferior */
    }
    .stSelectbox {
        margin-bottom: 20px;
        width: 50%;
        margin-left: auto;
        margin-right: auto;
    }
    footer {
        text-align: center;
        margin-top: auto; /* Coloca o rodapé na parte inferior */
        font-family: 'Segoe UI', sans-serif;
        color: #888;
    }
    </style>
    """, unsafe_allow_html=True)

languages_future = {
    "Python": """
**Python** continuará sendo uma das linguagens mais populares devido à sua versatilidade e à crescente demanda por ciência de dados, machine learning e desenvolvimento web. Sua sintaxe simples e legível torna Python acessível para iniciantes, ao mesmo tempo que proporciona poderosas funcionalidades para desenvolvedores experientes. A linguagem tem sido amplamente adotada em diversas áreas da tecnologia, desde automação de tarefas simples até o desenvolvimento de aplicações complexas de inteligência artificial.

Nos próximos anos, espera-se que novas bibliotecas e frameworks continuem a expandir as capacidades do Python, especialmente em áreas emergentes como análise de grandes volumes de dados (Big Data), desenvolvimento de algoritmos de deep learning, e automação de processos através de RPA (Robotic Process Automation). A comunidade ativa e a vasta quantidade de recursos disponíveis também garantem que Python se mantenha na vanguarda da inovação tecnológica.

Além disso, Python está se tornando uma escolha cada vez mais comum para o desenvolvimento de aplicações em áreas como bioinformática, finanças, e automação industrial, onde a integração com sistemas legados e a necessidade de análise de dados em tempo real são cruciais. Com o suporte contínuo de grandes empresas e a adoção em larga escala em ambientes corporativos e acadêmicos, Python está bem posicionado para manter e até expandir sua influência no ecossistema de desenvolvimento de software.

Com o surgimento de novos paradigmas de programação, como programação assíncrona e o desenvolvimento orientado a eventos, Python também está adaptando suas estruturas e bibliotecas para oferecer suporte a essas tendências. O futuro do Python parece promissor, com a linguagem continuando a ser uma escolha preferida para desenvolvedores que buscam combinar simplicidade com funcionalidade robusta.
""",
    "JavaScript": """
**JavaScript** manterá sua posição como a linguagem predominante para desenvolvimento web, tanto no frontend quanto no backend. Com a ascensão de frameworks como React, Angular e Vue.js, JavaScript se tornou a espinha dorsal das aplicações web modernas. Sua versatilidade é ampliada pelo Node.js, que permite o desenvolvimento de aplicações server-side usando a mesma linguagem. Além disso, a comunidade ativa e o ecossistema em constante evolução garantem que JavaScript continue a ser uma escolha popular para novos desenvolvimentos, especialmente com a crescente adoção de Progressive Web Apps (PWAs) e o desenvolvimento de aplicações móveis híbridas.

Com o suporte de ferramentas como TypeScript, que adiciona tipagem estática à linguagem, JavaScript continuará a evoluir para suportar novas tecnologias, como inteligência artificial no frontend, desenvolvimento de jogos e Internet das Coisas (IoT). O futuro do JavaScript parece brilhante, com a linguagem continuando a inovar e a expandir seus horizontes em novas áreas da tecnologia.

Além disso, JavaScript está se tornando uma escolha preferida para o desenvolvimento de plataformas interativas e dinâmicas, onde a experiência do usuário e a responsividade são cruciais. A linguagem também tem visto uma adoção crescente em áreas como automação de tarefas web, com bibliotecas e ferramentas que simplificam o trabalho dos desenvolvedores. Com a evolução contínua da web e a demanda por experiências mais ricas e interativas, JavaScript continuará a ser um pilar central no desenvolvimento de tecnologias modernas.
""",
    "Java": """
**Java** permanecerá como uma escolha sólida para desenvolvimento de software empresarial e aplicativos Android. Com décadas de maturidade, Java estabeleceu uma reputação de confiabilidade, desempenho e segurança, tornando-o uma escolha preferida para aplicações que exigem estabilidade a longo prazo. A evolução contínua da linguagem, com novas versões introduzindo funcionalidades modernas como expressões lambda, APIs de Streams e melhorias na coleta de lixo, permite que Java se adapte às necessidades modernas.

Em ambientes de nuvem e microserviços, Java continua a ser uma escolha popular devido à sua robustez e à ampla gama de ferramentas e bibliotecas disponíveis. O suporte contínuo de grandes empresas, como Oracle e IBM, e a adoção em larga escala em sistemas de grande porte garantem que Java esteja bem posicionado para continuar sua evolução, especialmente em áreas como machine learning, big data e blockchain.

Nos próximos anos, Java também deverá expandir sua presença em áreas como desenvolvimento de APIs, automação industrial e sistemas críticos, onde a confiabilidade e a escalabilidade são essenciais. A linguagem está cada vez mais adaptada às necessidades do desenvolvimento moderno, incluindo a capacidade de trabalhar de forma eficiente em ambientes de DevOps e de integração contínua. Além disso, Java tem sido um pilar importante na educação em ciência da computação, garantindo que as novas gerações de desenvolvedores estejam bem familiarizadas com seus conceitos e práticas.
""",
    "C++": """
**C++** continuará a ser a linguagem preferida para o desenvolvimento de sistemas de alto desempenho, como jogos, motores gráficos, e software de sistemas embarcados. Sua combinação de controle de baixo nível com recursos de alto nível a torna uma escolha ideal para aplicações que exigem desempenho e eficiência. C++ segue evoluindo com novos padrões, como C++20, que introduz funcionalidades como módulos, corrotinas e conceitos, aumentando a segurança e a eficiência da linguagem.

Além disso, C++ permanece relevante em áreas críticas, como desenvolvimento de sistemas operacionais, bancos de dados de alto desempenho e plataformas financeiras. Com uma forte comunidade e suporte contínuo para novas arquiteturas de hardware, C++ continuará a ser uma escolha robusta para desenvolvedores que buscam tirar o máximo proveito do hardware subjacente, mantendo-a relevante em aplicações onde o desempenho é crítico.

O futuro do C++ também inclui a adaptação a novas arquiteturas de hardware, como a computação quântica e os sistemas de inteligência artificial, onde a necessidade de desempenho máximo é uma constante. Com a crescente demanda por sistemas autônomos e de alto desempenho, C++ continuará a ser uma escolha indispensável para desenvolvedores que precisam otimizar ao máximo o uso dos recursos do sistema. A linguagem, com seu conjunto de ferramentas robusto e uma comunidade dedicada, está bem posicionada para continuar sendo uma pedra angular no desenvolvimento de software de alta performance.
""",
    "C#": """
**C#** terá um futuro promissor no desenvolvimento de jogos, especialmente com o Unity, que é uma das principais plataformas para o desenvolvimento de jogos multiplataforma. Além disso, C# continua a ser uma escolha popular para o desenvolvimento de aplicativos desktop e web com o .NET, que oferece uma plataforma integrada e um ambiente de desenvolvimento rico.

A adoção do .NET Core, que é multiplataforma e open-source, ampliou ainda mais o alcance do C#, permitindo o desenvolvimento em Windows, macOS e Linux. Com o crescimento do ecossistema de desenvolvimento de nuvem, especialmente com Azure, C# está bem posicionado para se expandir em novas áreas como inteligência artificial, automação e IoT. A linguagem continuará a se adaptar às novas tendências tecnológicas, como desenvolvimento assíncrono e programação reativa, garantindo seu lugar no futuro da programação.

Nos próximos anos, C# deverá fortalecer ainda mais sua presença em ambientes corporativos, onde a integração com sistemas legados e a capacidade de desenvolvimento rápido e seguro são essenciais. A linguagem também verá um crescimento na automação de processos empresariais e no desenvolvimento de soluções de inteligência artificial, onde a capacidade de trabalhar com grandes volumes de dados e a eficiência em ambientes distribuídos são cruciais. Com uma comunidade ativa e o suporte contínuo da Microsoft, C# continuará a ser uma escolha relevante para desenvolvedores que buscam criar aplicações inovadoras e escaláveis.
""",
    "Ruby": """
**Ruby** manterá uma comunidade fiel no desenvolvimento web, especialmente em startups e projetos que valorizam o desenvolvimento ágil e iterativo. Embora Ruby não seja tão popular quanto outras linguagens, ele é altamente valorizado por sua simplicidade e pela felicidade do desenvolvedor, um conceito central na filosofia da linguagem.

Ruby on Rails, em particular, permite o desenvolvimento rápido de aplicações web, com convenções que simplificam tarefas comuns. Nos próximos anos, Ruby continuará a evoluir, com novas versões trazendo melhorias em desempenho e segurança, enquanto mantém sua sintaxe limpa e expressiva. Embora enfrente concorrência de outras linguagens de script, Ruby continuará a ser uma escolha popular para desenvolvedores que priorizam produtividade e clareza de código. A linguagem também tem encontrado nichos em áreas como automação de processos e desenvolvimento de scripts personalizados, assegurando sua relevância no futuro.

Além disso, Ruby deverá expandir seu alcance para novas áreas de desenvolvimento, como automação de processos empresariais e a criação de ferramentas internas que exigem rapidez e flexibilidade. A linguagem, com sua forte ênfase na simplicidade e na satisfação do desenvolvedor, continuará a atrair uma base dedicada de usuários que apreciam sua filosofia e abordagem pragmática ao desenvolvimento de software. Com uma comunidade vibrante e o suporte de recursos amplamente disponíveis, Ruby está bem posicionado para continuar a ser uma escolha relevante para projetos que exigem agilidade e inovação.
""",
    "Go": """
**Go** (ou Golang) terá um crescimento contínuo em áreas como desenvolvimento backend, sistemas distribuídos e DevOps. Criada pela Google, Go é conhecida por sua simplicidade, eficiência e robustez, tornando-se uma escolha popular para arquiteturas de microserviços e sistemas escaláveis. A linguagem foi projetada com a concorrência em mente, o que a torna ideal para construir aplicações que precisam lidar com grandes volumes de tráfego ou processar muitas solicitações simultaneamente.

Nos próximos anos, Go continuará a ganhar tração, especialmente em projetos que exigem alta performance, como plataformas de streaming, sistemas de comunicação em tempo real e ferramentas de infraestrutura de nuvem. Além disso, a comunidade Go está ativamente desenvolvendo novas bibliotecas e frameworks que expandem suas capacidades, permitindo que a linguagem se adapte a novas tendências tecnológicas e mantenha sua relevância no desenvolvimento moderno de software.

O futuro do Go também inclui uma adoção mais ampla em áreas como desenvolvimento de ferramentas de automação, sistemas financeiros e tecnologias de segurança, onde a simplicidade e a eficiência da linguagem são altamente valorizadas. Go também está se tornando uma escolha preferida para o desenvolvimento de aplicações serverless e em nuvem, onde a capacidade de lidar com demandas de escala e complexidade é crucial. Com uma comunidade ativa e um ecossistema em crescimento, Go continuará a ser uma linguagem de destaque no desenvolvimento de soluções escaláveis e de alto desempenho.
""",
    "R": """
**R** continuará a ser uma ferramenta importante para análise de dados e estatísticas, especialmente em ambientes acadêmicos e de pesquisa. Embora a linguagem enfrente concorrência de Python, sua especialização em estatística, visualização de dados e manipulação de grandes volumes de dados assegura sua relevância no futuro.

R é amplamente utilizado por estatísticos, analistas de dados e cientistas de dados para realizar análises complexas, criar gráficos de alta qualidade e desenvolver modelos estatísticos avançados. A linguagem também se destaca em áreas como bioinformática, econometria e ciências sociais, onde é usada para desenvolver modelos preditivos e realizar análises rigorosas. Com uma vasta gama de pacotes disponíveis através do CRAN (Comprehensive R Archive Network), R continuará a evoluir para atender às necessidades de análise de dados emergentes, garantindo que permaneça uma escolha confiável para profissionais que trabalham com grandes conjuntos de dados e métodos estatísticos avançados.

Além disso, R deverá expandir seu uso em áreas como análise preditiva e ciência dos dados aplicada, onde a necessidade de lidar com grandes volumes de dados em tempo real é crescente. A linguagem, com sua forte ênfase em análise estatística rigorosa e visualização de dados, continuará a ser uma ferramenta essencial para pesquisadores e profissionais que precisam extrair insights significativos a partir de dados complexos. Com o suporte contínuo da comunidade acadêmica e de pesquisa, R está bem posicionada para manter sua relevância no futuro da análise de dados.
""",
    "C": """
**C** continuará a ser uma linguagem fundamental no desenvolvimento de sistemas de baixo nível, como sistemas operacionais, drivers e software embarcado. Com mais de quatro décadas de uso, C estabeleceu-se como uma linguagem altamente eficiente e flexível, sendo uma escolha popular em ambientes onde o controle direto sobre o hardware e a máxima eficiência de desempenho são cruciais.

Nos próximos anos, C permanecerá relevante em áreas onde a eficiência e o controle do sistema são essenciais, como em sistemas embarcados, desenvolvimento de firmware, e em aplicações críticas de segurança. A linguagem também continuará a ser ensinada em cursos de ciência da computação em todo o mundo, devido à sua importância histórica e à sua capacidade de introduzir conceitos fundamentais de programação.

Além disso, C continuará a ser amplamente utilizado em ambientes de desenvolvimento de sistemas, onde a necessidade de acesso direto ao hardware e a capacidade de otimizar o código para desempenho máximo são essenciais. O futuro de C também inclui sua adaptação a novas arquiteturas de hardware, como a computação quântica e os sistemas de alta performance, onde a linguagem poderá ser usada para desenvolver os componentes de base. Com uma comunidade dedicada e um conjunto de ferramentas robusto, C manterá sua posição como uma das linguagens mais importantes para o desenvolvimento de software de sistemas.
""",
    "Swift": """
**Swift** continuará a crescer como a principal linguagem para desenvolvimento de aplicativos iOS e macOS. Desenvolvida pela Apple, Swift foi projetada para ser rápida, segura e expressiva, permitindo que desenvolvedores criem aplicativos com menos código e maior facilidade de manutenção. Sua sintaxe moderna e funcionalidades poderosas têm atraído tanto desenvolvedores iniciantes quanto experientes.

Nos próximos anos, Swift deve expandir seu uso para além do ecossistema da Apple, com a possibilidade de se tornar mais popular no desenvolvimento de software para outras plataformas, como web e servidores, graças a projetos como o Swift for TensorFlow e a integração com frameworks de machine learning. A linguagem também continuará a evoluir para incorporar novas funcionalidades e otimizações, alinhando-se com as tendências emergentes da indústria.

Além disso, Swift verá um crescimento na adoção por empresas e desenvolvedores que buscam eficiência e segurança no desenvolvimento de aplicativos móveis e desktop. A linguagem também será fundamental para a criação de novas experiências de usuário em dispositivos Apple, como o Apple Vision Pro. Com o suporte contínuo da Apple e uma comunidade vibrante de desenvolvedores, Swift está bem posicionada para continuar a liderar o desenvolvimento de aplicativos no ecossistema Apple.
""",
    "Rust": """
**Rust** está se destacando como uma linguagem de programação focada em segurança de memória, eficiência e concorrência, tornando-a uma escolha cada vez mais popular para desenvolvimento de sistemas, jogos e até mesmo aplicações web. Criada pela Mozilla, Rust é conhecida por evitar muitos erros comuns de programação que ocorrem em linguagens como C e C++, oferecendo ao mesmo tempo desempenho de baixo nível.

Nos próximos anos, Rust deve expandir sua adoção em áreas críticas como desenvolvimento de sistemas operacionais, motores de jogos e software de infraestrutura, onde a segurança e a eficiência são essenciais. A linguagem também está ganhando tração em desenvolvimento web, com frameworks como Rocket e Actix, que estão mostrando a capacidade de Rust de combinar segurança com alta performance.

Rust também deve se tornar uma escolha preferida para o desenvolvimento de novos sistemas de blockchain e para projetos que requerem alta confiabilidade e eficiência. Com uma comunidade crescente e suporte de grandes empresas, como Microsoft e Amazon, Rust está bem posicionado para se tornar uma das linguagens mais importantes para o desenvolvimento de software seguro e eficiente no futuro.
""",
    "Kotlin": """
**Kotlin** continuará a ser a linguagem principal para o desenvolvimento de aplicativos Android, depois de ser oficialmente adotada pelo Google como a linguagem preferida para essa plataforma. Com uma sintaxe moderna e funcionalidades avançadas, Kotlin oferece uma experiência de desenvolvimento mais fluida e produtiva em comparação com Java, especialmente para desenvolvedores móveis.

Nos próximos anos, espera-se que Kotlin expanda sua presença para além do Android, com adoção crescente no desenvolvimento de aplicativos web e backend, especialmente com frameworks como Ktor. A linguagem também está ganhando popularidade para desenvolvimento multiplataforma, permitindo que desenvolvedores usem o mesmo código para criar aplicativos para Android, iOS e web.

Além disso, Kotlin continuará a evoluir com novas funcionalidades que melhoram a produtividade e a segurança do desenvolvedor. A linguagem também está sendo adotada em ambientes corporativos e acadêmicos, onde sua flexibilidade e eficiência são altamente valorizadas. Com o suporte contínuo do Google e uma comunidade ativa, Kotlin está bem posicionada para continuar seu crescimento e se tornar uma linguagem de escolha para desenvolvedores que buscam eficiência e inovação no desenvolvimento de software.
"""
}

languages_images = {
    "Python": "images/python_logo.webp",  
    "JavaScript": "images/javascript_logo.webp",
    "Java": "images/java_logo.png",
    "C++": "images/C++_logo.png",
    "C#": "images/csharp.png",
    "Ruby": "images/ruby_logo.png",
    "Go": "images/go_logo.png",
    "R": "images/R_logo.png",
    "C": "images/C_Logo.png",
    "Swift": "images/swift_logo.png",
    "Rust": "images/rust_logo.png",
    "Kotlin": "images/Kotlin_logo.png"
}

st.title("Qual é o futuro da sua linguagem favorita?")

with st.container():
    language = st.selectbox("Escolha uma Linguagem de Programação", list(languages_future.keys()), key="select_language")

    st.subheader(f"O futuro da linguagem {language}:")

    st.image(languages_images[language], use_column_width=False, width=150)
    st.write(languages_future[language])

st.markdown("---")

st.markdown("""
    <footer>
        <p>Desenvolvido por Luigi, Luis e Davi 💻</p>
    </footer>
    """, unsafe_allow_html=True)
