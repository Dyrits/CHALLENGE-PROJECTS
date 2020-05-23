// Function to return a random DNA base:
const returnRandBase = () => {
  const dnaBases = ["A", "T", "C", "G"];
  return dnaBases[Math.floor(Math.random() * 4)];
};

// Function to return a random single stand of DNA containing 15 bases:
const mockUpStrand = () => {
  const newStrand = [];
  for (let i = 0; i < 15; i++) {
    newStrand.push(returnRandBase());
  }
  return newStrand;
};

// Factory function to create pAequor:
const pAequorFactory = (specimenNum, dna) => {
  return {
    specimenNum, 
    dna,

    mutate() {
      let index = Math.floor(Math.random() * this.dna.length);
      let randomBase = this.dna[index];
      let indexMutation = Math.floor(Math.random() * 3);
      let mutation = ["A", "T", "C", "G"].filter(base => base !== randomBase)[indexMutation];
      this.dna.splice(index, 1, mutation);   
      return this.dna;
    },

    compareDNA(pAequor) {
      let commonDNA = this.dna.filter((base, index) => base === pAequor.dna[index]);
      console.log(`Specimen ${this.specimenNum} and Specimen ${pAequor.specimenNum} have ${Math.round(commonDNA.length / this.dna.length * 100)}% DNA in common.`);
    },

    willLikelySurvive() {
      return this.dna.filter(base => base === "C" || base === "G").length / this.dna.length >= 0.6;
    }
  }
}

// Function to create a specified ammount of high-rate surviving pAequor:
function createpAequor(quantity) {
  let specimenNum = 1;
  let survivingSpecimen = []
  while (specimenNum < quantity + 1) {
    let specimen = pAequorFactory(specimenNum, mockUpStrand())
    if (specimen.willLikelySurvive()) {
      survivingSpecimen.push(specimen);
      specimenNum++;
    }
  }
  return survivingSpecimen;
}

let survivingSpecimen = createpAequor(30);
console.log(survivingSpecimen);
