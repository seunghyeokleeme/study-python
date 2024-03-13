 1. 가상 환경 생성 python3 -m venv myenv 
 2. 가상 환경 활성화 source myenv/bin/activate
 3. 패키지 설치 pip3 install xlwings 
 4. 패키지 목록 저장 pip3 freeze > requirements.txt
 5. vscode 설정 단축키 : Command + Shift + P Python: Select Interpreter 클릭 후 가상 환경 선택 (myenv) 
 6. 가상 환경 비활성화 deactivate 
 7. 가상 환경 폴더 삭제 rm -rf myenv 
 8. vscode 설정 해제 단축키 : Command + Shift + P Python: Select Interpreter 클릭 후 기존 환경 선택 (글로벌) 
 9. 공용 공간 패키지 + 가상 환경 생성 python3 -m venv myenv --system-site-packages 
 10. 패키지 설치 (파일로부터) pip3 install -r requirements.txt 
 11. 가상 환경 내 패키지 목록 조회 pip3 list --local
