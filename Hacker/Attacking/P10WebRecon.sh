r="\e[31m"
g="\e[32m"
y="\e[33m"
n="\e[0m"

checkInstall() {
  local cmd=("ping" "whois" "nmap" "dig" "curl" "traceroute" "nslookup")
  for com in "${cmd[@]}"; do
     if ! command -v $com >/dev/null; then 
        echo "${r}Command not installed => $com${n}" 
        check=true
     fi
  done
  if [ "$check" = true ]; then
      exit 1
  fi
}
user_r() {
  read -p "Enter target web: " target
  
  if $target 2>/dev/null; then
      echo -e "${r}Please enter target web !! ${n}"
      exit 1
  fi
}
checkInstall
user_r 
echo  -e "Starting Web Reconnaissance $target"
file="recon_$target.txt"

echo -e "Reconnaissance $target " | tee -a $file
echo -e "${g}\n[+] Running ping $target ... ${n}" | tee -a $file
ping -c 4 $target | tee -a $file

echo -e "${g}\n[+] Running curl $target ... ${n}" | tee -a $file
curl -I $target | tee -a $file
echo -e "${g}\n[+] Running traceroute $target ... ${n}" | tee -a $file
traceroute $target | tee -a $file
echo -e "${g}\n[+] Running nslookup $target ... ${n}" | tee -a $file
nslookup $target | tee -a $file
nslookup -type=NS $target | tee -a $file
nslookup -type=TXT $target | tee -a $file
echo -e "${g}\n[+] Running whois $target ... ${n}" | tee -a $file
whois $target | tee -a $file

echo -e "${g}\n[+] Running dig $target ... ${n}" | tee -a $file
dig "$target" A | tee -a $file
dig "$target" NS | tee -a $file
dig "$target" MX | tee -a $file
dig "$target" TXT | tee -a $file
echo -e "${g}\n[+] Running Nmap $target ... ${n}" | tee -a $file
nmap -T4 -F $target | tee -a $file

echo "${y} All result saved to $file ${n}"
