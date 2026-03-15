# Prompts Utilizados

Neste documento, reuni os prompts (instruções) que utilizei para guiar a criação de cada classe e lógica de negócio deste projeto de Análise e Projeto de Sistemas.

---

### Questão 01: Conta de Luz
"Como engenheiro de software, crie uma classe ContaLuz com atributos privados para dataLeitura, numLeitura, kwGasto e valorPagar. Adicione métodos públicos para verificarMenor e verificarMaior consumo. Modele o código em Python usando Streamlit para exibir esses cálculos."

### Questão 02: Texto Saída
"Crie uma classe TextoSaida com atributos privados para tamanhoLetra, corFonte, corFundo e tipoComponente. Implemente métodos para configurar o estilo do texto e exibi-lo como um componente visual (Label, Edit ou Memo)."

### Questão 03: Boneco
"Modele uma classe Boneco com atributos privados para nome, posX, posY e direcao. Implemente métodos para mover o boneco no plano cartesiano e mudar sua direção. Gere uma interface em Streamlit para simular a movimentação."

### Questão 04: Horário de Remédios
"Crie classes Remedio e PlanilhaHorarios. A classe Remedio deve possuir atributos privados para os dados do paciente e medicamento, além de métodos para cadastrar e sugerir horários. Implemente a associação com PlanilhaHorarios para gerenciar atrasos."

### Questão 05: Gastos Diários
"Modele um sistema de gastos com classes Gasto e TipoGasto (usando Enumeração para forma de pagamento). Implemente a lógica para gerar um relatório mensal agrupando por tipo e forma de pagamento."

### Questão 06: Comanda Eletrônica
"Desenvolva classes Comanda, ItemComanda e Produto. Implemente o relacionamento de composição onde uma Comanda contém vários Itens, cada um vinculado a um Produto. Inclua método para calcular o total da conta."

### Questão 07: Lista de Compras
"Modele uma classe ItemCompra para controle de estoque de Carolina. Adicione atributos para produto, unidade, qtdMes, qtdCompra e precoEstimado. Implemente métodos para calcular o gasto total da lista."

### Questão 08: Coleção de CDs
"Crie uma classe CD com atributos privados para artista, titulo e anoLancamento. Implemente um método para cadastrar e listar os CDs em uma coleção usando Streamlit."

### Questão 09: CDs (Complexo)
"Crie um diagrama de classes para um sistema de CDs com CD, Musica e Musico. Represente os relacionamentos como atributos derivados. Defina as classes, atributos e multiplicidades, garantindo que um CD contenha várias músicas e artistas."

### Questão 10: Sala de Reunião
"Modele as classes Sala e Reserva. Implemente o método verificarDisponibilidade na classe Sala que valide data e hora, associando a uma lista de Reservas confirmadas."

### Questão 11: Hierarquia Base
"Refatore o sistema para utilizar herança. Crie uma superclasse Base (com id e nome) e faça com que as classes anteriores (ContaLuz, Remedio, etc.) herdem dela, demonstrando a reutilização de atributos comuns."