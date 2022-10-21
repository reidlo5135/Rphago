# **Rphago**
개인 프로젝트(TOY)<br>
<b>VERSION: 1.0.0</b><br>

## **Rphago?**
<b>Rphago</b>란 Naver Papago에서 제공하는 Papago 번역 API를 이용하여 사용자의 언어 입력과 선택을 토대로 번역을 해주는 사이트입니다. <br><br>

## <b>사용기술</b>
<span><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/html-E34F26?style=for-the-badge&logo=html5&logoColor=white">
<img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white">
<img src="https://img.shields.io/badge/JAVASCRIPT-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white"><br>
<img src="https://img.shields.io/badge/jquery-0769AD?style=for-the-badge&logo=jquery&logoColor=white">
<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
<img src="https://img.shields.io/badge/Intellij IDEA-000000?style=for-the-badge&logo=IntelliJ Idea&logoColor=white"></span>

- Frontend - Html, Css, JavaScript
- Backend - Django Framework, Python3
- Version Control - Git, GitHub
- IDE - IntelliJ IDEA Ultimate

## <b>주요기능</b>

### [서비스 주요 로직]
- <b>언어 번역 선택/입력</b> : 사용자가 번역을 원하는 언어의 종류와 텍스트를 화면(HTML)에서 입력 후 서버(django)로 전송
- <b>Papago 번역 API로 요청</b> : 서버는 수신받은 텍스트와 언어 종류를 토대로 Naver Papago API로 REST 요청
- <b>번역 결과 반환</b> : Papago API에서 응답한 결과를 다시 최초 화면에 비동기(jquery)로 표시

