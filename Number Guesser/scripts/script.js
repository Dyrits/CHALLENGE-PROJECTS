let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:
const generateTarget = () => Math.floor(Math.random() * 10);

const compareGuesses = (humanGuess, computerGuess, secretTargetNumber) => Math.abs(secretTargetNumber - humanGuess) <= Math.abs(secretTargetNumber - computerGuess);

const updateScore = (winner) => winner === "human" ? humanScore++ : computerScore++;

const advanceRound = () => currentRoundNumber++;