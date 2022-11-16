# 👕🔍 의류 이미지 검색 서비스

<p align="center">
  <br>
  <img src="https://user-images.githubusercontent.com/105893642/202207345-8d2d459a-a926-4a5f-a3db-1e7408f02006.png"> 
  welcome 페이지
  <br>
</p>
<br>

## 👐 프로젝트 소개

<p align="justify">
  연예인, 유명 셀럽, SNS를 통해 이쁜옷을 찾았지만 어느 브랜드인지? 어느 쇼핑몰에서 판매하는지? 모르는 소비자들을 위해 캡처 사진 한 장으로 비슷한 옷을 크롤링 해주는 사이트.
</p>

<br>

## 🚀 기술 스택
### Front-End
| JavaScript |  React   |  Node   |
| :--------: | :------: | :-----: |
|   <img src="https://user-images.githubusercontent.com/105893642/202210283-066fe621-f3c4-4ab1-8043-b8ca98368331.svg">    |   <img src="https://user-images.githubusercontent.com/105893642/202211207-c85fbd87-9b53-4cb1-8db2-454a5f9c0065.svg">  | <img src="https://user-images.githubusercontent.com/105893642/202211519-2f49a26a-a065-4683-ac9c-4ee3e7bc160a.svg"> |

### Back-End
| Java | Spring | SpringSecurity | Python | Flask |
| :--: | :----: | :------------: | :----: | :---: |
| <img src="https://user-images.githubusercontent.com/105893642/202215723-95a7b438-75cd-494f-a4bf-79da1fe06f82.png" width="100px"> | <img src="https://user-images.githubusercontent.com/105893642/202217018-336ba025-b27b-47f7-bec9-5753aaa5fafa.png" width="90px"> | <img src="https://user-images.githubusercontent.com/105893642/202217411-9b051531-b398-4237-be47-6b91f54173b9.png" width="100px"> | <img src="https://user-images.githubusercontent.com/105893642/202218035-25277248-5249-4aa3-a963-32a4d5e74e4a.png" width="90px"> | <img src="https://user-images.githubusercontent.com/105893642/202218978-4612b90c-e5c1-468f-b397-4055c68f830b.png" width="80px"> |

### DB
| MySQL |
| :---: |
| <img src="https://user-images.githubusercontent.com/105893642/202219901-cb27c717-17b6-4892-80cb-a281123cca60.png" width="100px"> |

<br>

## 🚀 구현 기능

### 로그인
<p align="center">
  <br>
  <img src="https://user-images.githubusercontent.com/105893642/202228738-44b95a11-93af-48e9-b970-7a22d0d11576.png"> 
  로그인 화면
  <br>
</p>

#### 👉 로그인 기능 설명
  1. ID, PW 입력 후 로그인 버튼 활성화
  2. DB에서 ID, PW 존재여부 검증 후 로그인 성공

### 회원가입
<p align="center">
  <br>
  <img src="https://user-images.githubusercontent.com/105893642/202229374-ecccddaa-02ef-42c9-9312-326a2585acd1.png"> 
  회원가입 화면
  <br>
</p>

#### 👉 회원가입 기능 설명
  1. 이름, 이메일, 아이디, 비밀번호를 통해 회원가입
  2. 한글이름이 아니면 예외 처리 후 가이드 문구 출력. ex) 한글이름이 아닙니다.
  3. 이메일 형식이 올바르지 않으면 예외 처리 후 가이드 문구 출력. ex) 올바른 이메일 형식이 아닙니다.
  4. 이메일 형식이 올바르면 중복체크 버튼 활성화
  5. 아이디에 특수문자가 포함되거나 5자 미만이면 예외 처리 후 가이드 문구 출력. ex) 특수문자를 제외해여 5자 이상으로 입력해 주세요.
  6. 아이디 형식이 올바르면 중복체크 버튼 활성화
  7. 중복 체크 버튼 클릭 시 DB에 존재 여부 검증 후 사용 가능(사용 가능한 이메일, 아이디입니다.) 사용 불가(이미 존재하는 아이디, 이메일입니다.)
  8. 특수문자를 포함하여 8자 이상이면 올바른 비밀번호
  9. 입력된 비밀번호와 동일여부 확인
  10. 모든 입력값이 정상이면 가입 완료하기 버튼 활성화
  11. 가입 완료 후 회원가입 안내 메일 발송 후 로그인 페이지로 이동
  

### 아이디 찾기
<p align="center">
  <br>
  <img src="https://user-images.githubusercontent.com/105893642/202229952-f9690c4d-9a42-4758-a281-2663fcd44f9f.png"> 
  아이디 찾기 화면
  <br>
</p>

### 비밀번호 찾기
<p align="center">
  <br>
  <img src="https://user-images.githubusercontent.com/105893642/202230417-5301f68a-11e7-4e61-8d67-6fcb8734857c.png"> 
  비밀번호 찾기 화면
  <br>
</p>

### 비밀번호 변경하기
<p align="center">
  <br>
  <img src="https://user-images.githubusercontent.com/105893642/202230829-37bbd507-8f07-4487-8864-3b68a4298238.png">
  비밀번호 변경하기 화면
  <br>
</p>

### 이미지 업로드 및 크롤링
<p align="center">
  <br>
  <img src="https://user-images.githubusercontent.com/105893642/202231224-8b042dcf-574e-4e25-9a80-6259b7b7c4d0.png">
  이미지 업로드 화면
  <br>
</p>

### 크롤링 결과
<p align="center">
  <br>
  <img src="https://user-images.githubusercontent.com/105893642/202232393-2a21c32c-06c3-476c-b43f-640e9f53a6c2.png">
  크롤링 결과 화면
  <br>
</p>

<br>


## 배운 점 & 아쉬운 점

<p align="justify">

</p>
