# 💻 Project Description of Programming Activities

Este repositório contém um conjunto de atividades práticas em Python, focadas em conceitos de programação orientada a objetos (POO), herança e polimorfismo. Cada atividade está organizada em pastas separadas, facilitando o acesso e a prática.

## Activity Descriptions

### Activity 01: Hierarchy of Geometric Shapes
**File**: activity01/main.py  
**Description**:  
Nesta atividade, criamos uma hierarquia de classes para representar formas geométricas. A classe base é chamada `Forma`, e as classes derivadas são `Círculo` e `Retângulo`. Para cada uma dessas classes, métodos são implementados para calcular a área e o perímetro.

### Activity 02: Vehicle Hierarchy
**File**: activity02/main.py  
**Description**:  
Criamos uma hierarquia de classes para representar veículos. A classe base é `Veículo`, e as classes derivadas incluem `Carro` e `Bicicleta`. Adicionamos métodos para definir atributos como `cor` e `modelo`, e permitimos a chamada de métodos em cadeia para configurar esses atributos de forma fluida.

### Activity 03: Calculator with Polymorphism
**File**: activity03/main.py  
**Description**:  
Nesta atividade, criamos uma classe chamada `Calculadora` com um método `somar`. Usamos polimorfismo para implementar a sobrecarga desse método, permitindo que ele funcione tanto com números inteiros quanto com strings, demonstrando como a mesma função pode se comportar de forma diferente com base no tipo de entrada.

### Activity 04: Vehicle Interface
**File**: activity04/main.py  
**Description**:  
Criamos uma interface chamada `Veículo`, com métodos `acelerar` e `frear`. Em seguida, implementamos classes concretas como `Carro` e `Bicicleta`, que fornecem suas próprias implementações desses métodos. A atividade demonstra como o polimorfismo pode ser utilizado para tratar diferentes tipos de veículos de maneira uniforme.

### Activity 05: Animal Sound Emission
**File**: activity05/main.py  
**Description**:  
Nesta atividade, criamos uma classe base chamada `Animal`, com um método `emitirSom`. As classes derivadas incluem `Cachorro`, `Gato` e `Pássaro`, que sobrescrevem o método `emitirSom` para cada tipo de animal. Criamos uma lista de animais e percorremos essa lista chamando o método `emitirSom`, demonstrando como o polimorfismo permite que diferentes tipos de animais emitam sons de maneira uniforme.

### Practical Challenge: Bank Account Management System
**File**: desafio/main.py  
**Description**:  
Este desafio envolve a criação de um sistema de gerenciamento de contas bancárias. Usamos herança e polimorfismo para criar diferentes tipos de contas (por exemplo, conta corrente e conta poupança) e métodos para realizar operações bancárias, como depósito, saque e consulta de saldo.

## How to Run

1. Navegue até a pasta da atividade desejada.
2. Execute o arquivo `main.py` usando o Python:

```bash
python main.py
