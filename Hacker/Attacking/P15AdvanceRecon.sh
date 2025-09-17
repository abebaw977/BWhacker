R='\033[0;31m'
G='\033[0;32m'
Y='\033[1;33m'
y='\033[0;33m'
B='\033[1;34m'
g='\033[0;37m'
N='\033[0m'

tools=( "ping" "nmap" "assetfinder" "whois" "curl" "dig" "nslookup")
ch=false
for tool in "${tools[@]}"; do
  if  ! command -v "$tool" &>/dev/null ; then
     echo -e "${R}[!] Tool '$tool' is not installed. Please install it to continue.${N}"
     ch=true
  fi
done
if [ "$ch" == "true" ] ; then
  exit 1
fi

read -p "Enter target site: " target
[[ -z "$target" ]] && echo "Please enter target site !! " && exit 1
is_alive() {
  ping -c1 "$1" >/dev/null 2>&1
  if [ $? -eq 0 ]; then
     echo -e "$Y [*] $1 is alive $N"
  else
     echo -e "$R [!] $1 host is unreachable $N"
  fi
}
is_alive "${target##*//}"
read -p "Do you went continueb y/n: " cont
if [ "${cont,,}" != "y" ]; then
    exit 1
fi
url="${target%.com}"
url="${url##*//}"
File="recon-$url.txt"
echo -e "\n${G}@============== Starting Web Reconnaissance ========== ${N}" | tee -a "$File"
function saveR(){
  echo -e "$1" >> "$File"
}

if [[ "$target" == https://* || "$target" == http://* ]]; then
    Ftarget="$target"
else
    Ftarget="https://$target"
fi

echo "Ftarget is => $Ftarget"

echo -e "${B}[*] Running WHOIS on $target...${N}"
saveR "\n======== WHOIS ========"
whois $target  &>/dev/null >> "$File"

echo -e "${B}[*] Running CURL on $target...${N}"
saveR "\n======= curl ====="
curl -I $target &>/dev/null >> "$File"

echo -e "${B}[*] Running NSKOOKUP on $target...${N}"
saveR "\n===== nsloockup ====="
nslookup $target 2>&1 >> "$File"

echo -e "${B}[*] Running DIG on $target...${N}"
saveR "\n======= DIG ======="
dig $target ANY +noall +answer 2>&1 >> "$File"

echo -e "${B}[*] Running NMAP on $target...${N}"
saveR "\n===== NMAP ====="
nmap -T4 -p 21-550 -sV $target 2>&1 >> "$File"

echo -e "${B}[*] Enumerating subdomains with assetfinder...${N}"
saveR "\n===== Subdomains (assetfinder) ====="
assetfinder --subs-only $target 2>&1 >> "$File"


echo -e "${G}[+] Recon complete.${N}"
echo -e "${Y}[+] Report saved to: $File${N}"

echo -e "${B}[*] #======= Subdomains Bruite Force =======# $N"
subdomains=(
  www web webmail mail smtp imap pop ftp sftp
  )

for sub in "${subdomains[@]}"; do
  host="${sub}.${target}"
  res=$(curl -s --max-time 2 -I "https://${host}" 2>/dev/null | sed -n '1p')

  if [[ -n "$res" ]]; then
    echo -e "$y [*] (subD) $host => $res $N"
  else
    echo -e "$g [X] (subD) $host => no response $N"
  fi
done
echo -e "${B}[*] #======= Directory Bruite Force =======# $N"

commonDir=(
  admn backups old archive archives config configs configuration settings shop store
)
for dir in "${commonDir[@]}"; do
  host="${target}/$dir"
  res=$(curl -s --max-time 2 -I "https://${host}" 2>/dev/null | sed -n '1p')

  if [[ -n "$res" ]]; then
    if [[ "$res" != *"404"* ]]; then
      echo -e "$y [*] (Dir) $host => $res $N"
    fi
  else
    echo -e "$g [X] (Dir) $host => no response $N"
  fi
done

i=1
echo -e "${Y}[*] Extracting emails from ${Ftarget}...${N}"
emails=$(curl -s "$Ftarget" | grep -Eio '\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b' | sort -u | tr 'A-Z' 'a-z')

if [[ -z "$emails" ]]; then
    echo -e "${G} [X] No emails found.${N}"
else
    while IFS= read -r email; do
        echo -e "${G}${i})${N} $email"
        ((i++))
    done <<< "$emails"
fi
