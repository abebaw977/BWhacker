//  Counter projects-1

let start = 0

function Inta() {
  let text = document.getElementById("counter-value");
  text.textContent = start
}
document.getElementById("inc").addEventListener("click", function() {
  Inta()
  start++
})
document.getElementById("dec").addEventListener("click", function() {
  Inta()
  start--
  if (start < 1) {
    start = 0
  }
})
document.getElementById("res").addEventListener("click", function() {
  start = 0
  document.getElementById("counter-value").textContent = start
})




//  Clock projects-2



let clockValue = document.getElementById("clock-value")
let DataCond = document.getElementById("DateCond")
const now = new Date();
let Hours = now.getHours();
let Miuntes = now.getMinutes();
let Second = now.getSeconds();
let AmPm = "AM"
if (Hours > 12) {
  AmPm = "PM"
}
for (let x = 0; x < 100000; x++) {
  setTimeout(() => {
    Second++;
    if (Second == 60) {
      Second = 0
      setTimeout(() => {
        Miuntes++;
        console.log("Start Miuntes:", Miuntes)
        if (Miuntes == 60) {
          Miuntes = 0
          setTimeout(() => {
            Hours++;
          }, 0)
        }
      }, 0)
    }
    clockValue.textContent = Hours + ":" + Miuntes + ":" + Second + " " + AmPm;
  }, x * 1000)
}
const mName = now.toLocaleString('default', { month: 'long' });
const mNumber = now.getMonth() + 1;
const year = now.getFullYear();
const day = now.getDay();
DataCond.textContent = year + "/" + mNumber + "" + "/" + day;



// Qoute projects-3

let QFound = false;
let Qoute = document.getElementById("text");
let Qauth = document.getElementById("aut");
let Qtext = document.getElementById("text");
let Qr = Math.floor(Math.random() * 10)
let Qload = document.getElementById("lod")
let Perr = document.getElementById("err");
let con = [{
  text: "The only way to do great work is to love what you do.",
  author: "Steve Jobs",
},
{
  text: "Strive not to be a success, but rather to be of value.",
  author: "Albert Einstein",
},
{
  text: "The future belongs to those who believe in the beauty of their dreams.",
  author: "Eleanor Roosevelt",
}, ]
Qauth.textContent = con[2].author
Qtext.textContent = con[2].text

function Random() {
  let r = Math.floor(Math.random() * 3)
  Qauth.textContent = con[r].author
  Qtext.textContent = con[r].text
}

function Online() {
  Qload.style.display = "block"
  Qoute.style.display = "none"
  let options = {
    method: "GET",
    headers: {
      accept: 'application/json',
      'x-happi-token': 'hk318-kqHWrigUbzgDt7EngReMfiYXuhZo4Xuwmj'
    }
  }
  fetch("https://api.happi.dev/v1/quotes?language=EN&limit=10&related_to=string", options)
    .then(res => res.json())
    .then(res => {
      Qauth.textContent = res.quotes[Qr].author
      Qtext.textContent = res.quotes[Qr].quote
      Qload.style.display = "none"
      Qoute.style.display = "block"
      QFound = true
      Perr.textContent = ""
    })
    .catch(e => {
      if (QFound != true) {
        Perr.textContent = e;
      }
    })
}



// Background change project-4


let colorValue = document.getElementById("color");
let Cmp = window.getComputedStyle(document.body)
colorValue.textContent = Cmp.getPropertyValue("background-color")
document.getElementById("ChangeBg").addEventListener("click", function() {
  let red = Math.floor(Math.random() * 255).toString();
  let green = Math.floor(Math.random() * 255).toString();
  let blue = Math.floor(Math.random() * 255).toString();
  let color = "rgb(red,green,blue)"
  document.body.style.backgroundColor = "rgb(" + red + "," + green + "," + blue + ")";
  colorValue.textContent = "rgb(" + red + "," + green + "," + blue + ")";
});


// To-Do project-5


let Tcount = 0

function Add() {
  let Area = document.getElementById("ListArea");
  let inputs = document.getElementById("inputs").value;
  if (inputs == "") {
    return alert("Yaha")
  }
  Tcount++
  let task = document.createElement("div")
  let para = document.createElement("div");
  let re = document.createElement("div")
  re.className = "re"
  para.className = "value";
  task.className = "task"
  re.onclick = () => {
    task.remove()
    Tcount--;
  }
  
  re.textContent = "x"
  para.textContent = Tcount + ". " + inputs;
  
  task.appendChild(para)
  task.appendChild(re)
  Area.appendChild(task)
  
  document.getElementById("inputs").value = ""
}


//BMI cal project-6


function cal() {
  let vv = document.getElementById("values")
  let v = document.getElementById("values-m")
  
  let he = parseInt(document.getElementById("height").value)
  let wi = parseInt(document.getElementById("weight").value)
  let res = wi / he * 2
  if (isNaN(he) || he <= 0 || isNaN(wi) || wi <= 0) {
    vv.textContent = "Please enter valid numbers!";
    v.textContent = "";
    return;
  }
  vv.textContent = "Your BMI: " + res.toFixed(2);
  if (res < 18.5) {
    v.textContent = "Underweight"
  } else if (res >= 18.5 || res <= 24.9) {
    v.textContent = "Normal"
  } else if (res >= 25 || res <= 29.9) {
    v.textContent = "Overweight"
  } else {
    v.textContent = "Obuse"
  }
}

// Palindirom project-7

function checkP() {
  let pi = document.getElementById("pinput").value.trim()
  let pr = document.getElementById("preuslt")
  let x = ""
  
  pi = pi.toLowerCase().replace(/\s/g, "")
  
  let Result = pi.split("").reverse().join("")
  let Final = (Result == pi) ? "Yes, it’s a palindrome" : "No, not a palindrome ";
  pr.textContent = Final
}


// Tip-Cal projects-8

function TipC() {
  let per = parseInt(document.getElementById("myDropdown").value)
  let bill = parseFloat(document.getElementById("bill").value)
  let pe = parseFloat(document.getElementById("Np").value)
  let tip = document.getElementById("tip")
  let ttp = document.getElementById("ttp")
  if (isNaN(bill) || isNaN(pe) || pe === "") {
    return alert("It is empty")
  }
  let tips = bill * (per / 100)
  let tipPP = tips / pe
  let totalPP = (bill + tips) / pe
  
  tip.textContent = "Tip per person: $" + tipPP.toFixed(2);
  ttp.textContent = "Total per person: $" + totalPP.toFixed(2);
}

// Weather project-9

function searchW() {
  let city = document.getElementById("city").value
  let data = document.getElementById("data")
  let api = "You api key"
  if (city === "") {
    return alert("Enter city")
  }
  fetch(`http://api.weatherapi.com/v1/current.json?key=7d4f3586e10e4c65909144016252108&q=${city}`)
    .then(res => res.json())
    .then(res => {
      let city = res.location.name
      let region = res.location.region
      let country = res.location.country
      let temp = res.current.condition.text
      
      data.innerHTML = `
        City: ${city} <br> 
        Region: ${region} <br>
        Country: ${country} <br>
        Temperature: ${temp} `
      
    })
}


//Slider Project 10


let imgS = document.querySelector(".img"); // match your HTML: class="img"
let imgs = document.querySelectorAll(".img img").length;

let indexS = 0;

function slides(i) {
  if (i < 0) {
    indexS = imgs - 1; // go to last image if < 0
  } else if (i >= imgs) {
    indexS = 0; // loop back to first image
  } else {
    indexS = i;
  }
  imgS.style.transform = `translateX(${-indexS * 100}%)`;
}

function prev() {
  slides(indexS - 1);
}

function next() {
  slides(indexS + 1);
}

// autoplay
setInterval(() => {
  slides(indexS + 1);
}, 3000);







let array = []
let tables = document.getElementById("table")

function refrash() {
  tables.innerHTML = ""
  let item = JSON.parse(localStorage.getItem("arrays")) || [];
  tables.innerHTML = `<tr>
      <th>Expense</th>
      <th>Amount</th>
      <th>Catagory</th></tr>`
  item.forEach(function(items) {
    let tr = document.createElement("tr")
    tr.innerHTML = `
          <td>${items.name}</td>
          <td>${items.amount}</td>
          <td>${items.catagory} <p onclick=remove(${items.id})>x</p></td>
          `
    
    tables.appendChild(tr)
  })
}

function AddItem() {
  let items = JSON.parse(localStorage.getItem("arrays")) || [];
  let name = document.getElementById("name").value
  let amount = parseInt(document.getElementById("amount").value)
  let catagory = document.getElementById("catagory").value
  if (isNaN(amount) || amount === "" || name === "" || catagory === "") {
    if (isNaN(amount)) {
      return alert("Amount must only number")
    }
    return alert("please,Enter correct from")
  }
  items.push({ id: Date.now(), name: name, amount: amount, catagory: catagory })
  localStorage.setItem("arrays", JSON.stringify(items));
  
  refrash()
  document.getElementById("name").value = "";
  document.getElementById("amount").value = 0;
}

function remove(id) {
  let items = JSON.parse(localStorage.getItem("arrays")) || [];
  let fileters = items.filter(it => it.id !== id);
  localStorage.setItem("arrays", JSON.stringify(fileters))
  refrash()
}
refrash()


let corr = document.getElementById("corr");
let sc = document.getElementById("sc")
let m = [
  { qus: "According to Newton's second law of motion, force (F) is equal to mass (m) multiplied by what?", ch: ["Velocity (v)", "Acceleration (a)", "Momentum (p)", "Jerk (j)"], ans: "B" },
  { qus: "What is the formula for kinetic energy (K) in terms of mass (m) and velocity (v)?", ch: ["K = m*v", "K = ½*m*v²", "K = F*d", "K = m*g*h"], ans: "B" },
  { qus: "The gravitational potential energy (U) near the Earth's surface is calculated by which formula?", ch: ["U = m*g", "U = ½*k*x²", "U = m*g*h", "U = F*d"], ans: "C" },
  { qus: "In physics, work (W) is defined as force (F) multiplied by what other quantity?", ch: ["Time (t)", "Mass (m)", "Velocity (v)", "Displacement (d)"], ans: "D" },
  { qus: "Power (P) is the rate of doing work (W). What is the correct formula for power in terms of work and time (t)?", ch: ["P = W*t", "P = F*v", "P = W / t", "P = ΔE"], ans: "C" }
]
let Qcurrent = 0;
let Qscore = 0

function check() {
  if (Qcurrent >= m.length) {
    finshed()
    return
  }
  let qu = document.getElementById("qu")
  let ch = document.getElementById("choice")
  /*for (x in Question){
    qu.innerHTML=Question[x]
    for (y in choice){
      console.log((choice[y].A))
    }*/
  let q = m[Qcurrent]
  qu.textContent = (Qcurrent + 1) + ". " + q.qus
  ch.innerHTML = `
        <p onclick="ans('A')" ><b>A.  ${q.ch[0]}</b>
        <p onclick="ans('B')" ><b>B.  ${q.ch[1]}</b>
        <p onclick="ans('C')" ><b>C.  ${q.ch[2]}</b>
        <p onclick="ans('D')"><b>D.  ${q.ch[3]}</b>
      
        `
}
check()

function ans(val) {
  let Qcorrect = m[Qcurrent].ans;
  if (Qcorrect === val) {
    Qscore++;
    corr.textContent = "Correct"
    corr.style.color = "green"
  } else {
    corr.textContent = "Wrong"
    corr.style.color = "red"
  }
  setTimeout(function() {
    Qcurrent++
    check()
    corr.textContent = ""
  }, 1000)
}

function nextQ() {
  Qcurrent++;
  check()
}

function prevQ() {
  Qcurrent++;
  check()
}

function finshed() {
  document.getElementById("qu").style.display = "none";
  document.getElementById("choice").style.display = "none";
  document.getElementById("next").style.display = "none";
  corr.style.display = "none";
  sc.style.display = "block"
  sc.textContent = "Score:" + Qscore;
}









const editor = document.getElementById("editior");
const preview = document.getElementById("prev");



function insert(text) {
  editor.value += text;
  render();
}

function render() {
  preview.innerHTML = "";
  
  let lines = editor.value.split("\n");
  
  lines.forEach(line => {
    let html = line;
    
    
    if (line.startsWith("### ")) {
      html = `<h3>${line.slice(3).trim()}</h1>`;
    }
    else if (line.startsWith("##")) {
      html = `<h2>${line.slice(2).trim()}</h2>`;
    }
    else if (line.startsWith("#")) {
      html = `<h1>${line.slice(2).trim()}</h1>`;
    }
    html = html.split("**").map((t, s) => s % 2 === 1 ? `<b>${t}</b>` : t).join("");
    html = html.split("*").map((t, s) => s % 2 === 1 ? `<i>${t}</i>` : t).join("");
    
    
    
    let st = html.indexOf("[");
    let m = html.indexOf("](");
    let en = html.indexOf(")", m);
    
    if (st !== -1 && m !== -1 && en !== -1) {
      alert(html)
      let text = html.slice(st + 1, m);
      let url = html.slice(m + 2, en);
      html = html.slice(0, st) + `<a href="${url}" target="_blank">${text}</a>` + html.slice(en + 1);
      
      /* 
      st = html.indexOf("[", st + 1);
      m = html.indexOf("](", st);
      en = html.indexOf(")", m);*/
    }
    
    preview.innerHTML += html + "<br>";
  });
}



function SearchA() {
  let apiS = document.getElementById("apiS").value
  if (apiS === "") return
  fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${apiS}`)
    .then(res => res.json())
    .then(res => {
      try {
        let name = res.meals[0].strMeal
        let image = res.meals[0].strMealThumb.split("\ ")
        let desc = res.meals[0].strInstructions;
        alert(desc)
        for (let i = 0; i < res.meals.length; i++) {
          document.getElementById("results").innerHTML += `<div class="boxs"><img src='${res.meals[i].strMealThumb.split("\ ")}' alt="Not Foud Image" /><p class="name">${res.meals[i].strMeal}</p><span>${desc}</span></div>`;
          //alert(res.meals[i].strMeal)
        }
      }
      catch (e) {
        alert(e)
      }
    })
}
//apiS.addEventListener("input", AoutRun)
// AoutRun()








function SearchM() {
  let movieS = document.getElementById("movieS").value
  if (movieS === "") return
  fetch(`https://www.omdbapi.com/?t=${movieS}&apikey=a1826000`)
    .then(res => res.json())
    .then(res => {
      try {
        document.getElementById("imgM").innerHTML = `<img class="imgM" src='${res.Poster}' alt="Image Not Found" />`
        document.getElementById("info").innerHTML = `<div class="boxsM">
               <h2>${res.Title}</h1>
               <p>Released in ${res.Year}</p>
               <p>${res.Plot}</p>
                 <p>Director : ${res.Director}</p>
                 <p>Time : ${res.Runtime}</p>
                 <p>Released Time : ${res.Released}</p>
                 <p>Writer : ${res.Writer}</p>
                 <p>Action : ${res.Action}</p>
                 <p>Actors : ${res.Actors}</p>
                 <p>Languages : ${res.Language}</p>
                 <p>Country : ${res.Country}</p></div>`;
      }
      catch (e) {
        alert(e)
      }
    })
}







let Random1 = [
  { "text": "The quick brown fox jumps over the lazy dog." },
  { "text": "Typing fast requires accuracy as well as speed." },
  { "text": "Practice daily to improve your typing skills." },
  { "text": "Consistency is the key to becoming a better typist." },
  { "text": "Keyboard shortcuts can save time in everyday tasks." },
  { "text": "Focus on posture and hand position while typing." },
  { "text": "Technology evolves quickly, so adaptability is vital." },
  { "text": "Clear communication often depends on fast typing." },
  { "text": "Errors reduce speed, so aim for precision first." },
  { "text": "Typing challenges can be fun and highly motivating." }
];

let timerInterval, checkInterval;
let timeLeft = 60;
let originalWords = [];

function startTimer(finishFlag) {
  timeLeft = 60;
  const Time = document.getElementById("Time");
  Time.textContent = `Time: ${timeLeft}s`;
  
  timerInterval = setInterval(() => {
    timeLeft--;
    Time.textContent = `Time: ${timeLeft}s`;
    
    if (timeLeft <= 0) {
      clearInterval(timerInterval);
      clearInterval(checkInterval);
      Time.textContent = "Time finished";
      finishFlag.f = true;
      document.getElementById("spell").disabled = true;
    }
  }, 1000);
}

function checkSp(original, typed) {
  let errors = 0,
    correct = 0;
  for (let i = 0; i < typed.length; i++) {
    if (typed[i] === original[i]) {
      correct++;
    } else {
      errors++;
    }
  }
  return { errors, correct };
}

function updateResults() {
  const typedWords = document.getElementById("spell").value.trim().split(/\s+/);
  if (typedWords[0] === "") return; // skip if nothing typed yet
  
  const { errors, correct } = checkSp(originalWords, typedWords);
  const wpm = ((typedWords.length / (60 - timeLeft + 1)) * 60).toFixed(0);
  const accuracy = ((correct / typedWords.length) * 100).toFixed(1);
  
  document.getElementById("wpm").textContent = `WPM: ${wpm}`;
  document.getElementById("acur").textContent = `Accuracy: ${accuracy}%`;
  document.getElementById("err").textContent = `Errors: ${errors}`;
}

function Start() {
  const randomText = Random1[Math.floor(Math.random1() * Random.length)].text;
  document.getElementById("textA").value = randomText;
  originalWords = randomText.trim().split(/\s+/);
  
  const spell = document.getElementById("spell");
  spell.value = "";
  spell.disabled = false;
  spell.focus();
  
  let finished = { f: false };
  startTimer(finished);
  
  spell.addEventListener("input", updateResults);
  
  checkInterval = setInterval(() => {
    if (finished.f) {
      clearInterval(checkInterval);
    }
  }, 500);
}







let TimeTime = 0
const Tst = []
let Tcon = true
let Ti = 60
let Tm = 25;

function RunS() {
  let timer = document.getElementById("timer");
  for (let x = 0; x < 25 * 60; x++) {
    const t = setTimeout(() => {
      let leftTime = TimeTime
      if (!Tcon) return;
      Ti--
      if (Ti == 0) {
        Tm--
        if (Tm == 0) {
          Tst.forEach(clearTimeout)
          Ti = 0
        } else { Ti = 59 }
      }
      if (Tm > 5) {
        document.getElementById("status").innerHTML = "Working .."
      } else {
        document.getElementById("status").innerHTML = "Breaking .."
      }
      TimeTime = `${Tm} : ${Ti}`;
      timer.textContent = TimeTime
    }, x * 1000)
    Tst.push(Tt)
  }
}

document.getElementById("starts").addEventListener("click", () => {
  Tcon = true
  RunS()
})
document.getElementById("stops").addEventListener("click", () => {
  if (Tcon) {
    let timer = document.getElementById("timer");
    Tst.forEach(clearTimeout)
    Tcon = false
  }
})
document.getElementById("resets").addEventListener("click", () => {
  console.log(TimeTime)
  let timer = document.getElementById("timer");
  Tst.forEach(clearTimeout)
  timer.innerText = "25:00"
})










document.getElementById("generate").addEventListener("click", () => {
  let res = document.getElementById("result");
  let len = document.getElementById("length");
  let u = document.getElementById("upper"); // fixed
  let l = document.getElementById("lower");
  let n = document.getElementById("nums");
  let s = document.getElementById("syms");
  
  let capital = [];
  let small = [];
  let Symbol = "!@#$%^&*()";
  let num = "1234567890";
  let Gcapital = "";
  let Gsmall = "";
  let Gsymbol = "";
  let Gnum = "";
  
  for (let x = 65; x <= 90; x++) {
    capital.push(String.fromCharCode(x));
  }
  for (let x = 97; x <= 122; x++) {
    small.push(String.fromCharCode(x));
  }
  
  let count = len.value == 8 ? 2 : len.value == 12 ? 3 : 0;
  if (count === 0) {
    res.value = "Password Length must only be 8 or 12";
    return;
  }
  
  for (let r = 0; r < count; r++) {
    Gcapital += capital[Math.floor(Math.random() * capital.length)];
    Gsmall += small[Math.floor(Math.random() * small.length)];
    Gsymbol += Symbol[Math.floor(Math.random() * Symbol.length)];
    Gnum += num[Math.floor(Math.random() * num.length)];
  }
  
  
  res.value =
    (u.checked ? Gcapital : "") +
    (l.checked ? Gsmall : "") +
    (n.checked ? Gnum : "") +
    (s.checked ? Gsymbol : "");
});













document.getElementById("searchBtn").addEventListener("click", () => {
  let searchD = document.getElementById("searchD").value
  if (searchD === "") return
  fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${searchD}`)
    .then(res => res.json())
    .then(res => {
      if (!res || res.title === "No Definitions Found") {
        document.getElementById("resultD").innerHTML = `
          <div class="resu">
            <h2>No results found</h2>
            <p>Try searching another word.</p>
          </div>`;
        return;
      }
      const fd = res[0].meanings[0];
      const sd = res[0].meanings[1] || fd;
      const pho = res[0].phonetics[0] ? res[0].phonetics[0].text : '';
      const audio = res[0].phonetics[0] ? res[0].phonetics[0].audio : '';
      const word = res[0].word;
      const definition = fd.definitions[0].definition;
      const example = fd.definitions[0].example || "None";
      const syn = fd.synonyms.length ? fd.synonyms.join(", ") : "None";
      const ant = fd.antonyms.length ? fd.antonyms.join(",") : "None";
      const pos = sd.partOfSpeech;
      alert(audio)
      document.getElementById("resultD").innerHTML = `
          <div class="resu">
          <h2>${word}</h2>
          <div class="pho">${pho}</div>
          <div class="defination">
          <p><strong>Defination:</strong> ${definition}</p>
          <p class="example">Example: ${example}</p>
          </div>
          <div class="about">
            <p><strong>Synonyms: ${syn}</strong></p>
            <p><strong>Antonyms: ${ant}</strong></p>
            <p><strong>Part Of Speech: ${pos}</strong></p>
            <p  class="audio" onclick="Play('${audio}')" >🔊 Yes</p>
          </div></div>`;
    });
});

function Play(music) {
  let audio = new Audio(music)
  audio.play()
}