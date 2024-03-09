let equationBlocks = [];
let setNumbers = [];

// Generate a set of random numbers for each row
for (let i = 0; i < 5; i++) {
    const setNumber = Math.floor(Math.random() * 10) + 1;
    setNumbers.push(setNumber);
    document.getElementsByClassName('setNumber')[i].innerHTML = setNumber;
}

let currentRow = 0;
const numberRows = 5;
let score = 0;

function addNumber(number) {
    if (currentRow >= numberRows) {
        return;
    }

    equationBlocks[currentRow].push(number);
    updateEquationDisplay();
}

function addOperator(operator) {
    if (currentRow >= numberRows) {
        return;
    }

    equationBlocks[currentRow].push(operator);
    updateEquationDisplay();
}

function deleteInput() {
    if (currentRow < 0) {
        return;
    }
    const currentEquation = equationBlocks[currentRow];
  const lastBlockIndex = currentEquation.length - 1;

  if (lastBlockIndex >= 0) {
    // Clear the content of the current block
    const currentBlockId = `block${currentRow + 1}-${lastBlockIndex + 1}`;
    document.getElementById(currentBlockId).value = '';
    equationBlocks[currentRow].pop(); // Remove the last element from the array
  }
}

function updateEquationDisplay() {
    const currentEquation = equationBlocks[currentRow];
    for (let i = 0; i < currentEquation.length; i++) {
        document.getElementById(`block${currentRow + 1}-${i + 1}`).value = currentEquation[i];
    }
}

function calculate() {
    if (currentRow >= numberRows) {
        return;
    }

    const currentEquation = equationBlocks[currentRow];
    const equation = currentEquation.join('');
    if (equation.length !== 5) {
        return;
    }
    const result = eval(equation);
    const resultDiv = document.getElementsByClassName('result')[currentRow];

    const icon = document.createElement('span');
    icon.classList.add('result-icon');

    if (result === setNumbers[currentRow]) {
        icon.innerHTML = '&#10004;'; // Green tick
        icon.classList.add('correct');
        score++;
    } else {
        icon.innerHTML = '&#10008;'; // Red cross
        icon.classList.add('incorrect');
    }

    resultDiv.appendChild(icon);
    disableInputs();
    equationBlocks.push([]);
    currentRow++;
    if (currentRow < numberRows) {
        enableInputs();
    }
    if (currentRow >= numberRows) {
        showScore();
    }
}

function showScore() {
    const scoreDiv = document.querySelector('.score');
    scoreDiv.textContent = `SCORE: ${score} / ${numberRows}`;
}

function disableInputs() {
    const currentEquation = equationBlocks[currentRow];
    for (let i = 0; i < currentEquation.length; i++) {
        document.getElementById(`block${currentRow + 1}-${i + 1}`).disabled = true;
    }

    document.getElementById('deleteButton').disabled = true;
    document.getElementById('calculateButton').disabled = true;
}

function enableInputs() {
    const currentEquation = equationBlocks[currentRow];
    for (let i = 0; i < currentEquation.length; i++) {
        document.getElementById(`block${currentRow + 1}-${i + 1}`).disabled = false;
    }

    document.getElementById('deleteButton').disabled = false;
    document.getElementById('calculateButton').disabled = false;
}

function playAgain() {
    location.reload();
}

// Initialize the first row of equation blocks
equationBlocks.push([]);
enableInputs();