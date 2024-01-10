//import { FillMaskOutput, HfInference } from "@huggingface/inference";

const HF_ACCESS_TOKEN = "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";

console.log("Hello World!");

const fetch = require('node-fetch');

const res = fetch('http://www.google.com');

let x = 'Out: ';

// this is where we need to process the response
// as we cannot get what we need directly
res.then((response) => {
  return response.text();
}).then((body) => {
    x += '2';
    x += body;
    //console.log('In: ' + body);
});


const HfInference = require("@huggingface/inference").HfInference;

const FillMaskOutput = require("@huggingface/inference").FillMaskOutput;

const hf = new HfInference(HF_ACCESS_TOKEN);  

