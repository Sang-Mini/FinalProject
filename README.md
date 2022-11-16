# 👕🔍 의류 이미지 검색 서비스

<p align="center">
  <br>
  <img src="https://user-images.githubusercontent.com/105893642/202248430-780b1497-c8e0-4059-af23-7b47eaf0f3c4.gif">
  <br>
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

### AI
| Python | PyTorch | Flask |
| :----: | :-----: | :---: |
| <img src="https://user-images.githubusercontent.com/105893642/202218035-25277248-5249-4aa3-a963-32a4d5e74e4a.png" width="90px"> | <img src="https://user-images.githubusercontent.com/105893642/202252672-d04efd85-edf0-4a80-843a-f22568a36a88.png" width="100px"> | <img src="https://user-images.githubusercontent.com/105893642/202218978-4612b90c-e5c1-468f-b397-4055c68f830b.png" width="80px"> |

### DB
| MySQL |
| :---: |
| <img src="https://user-images.githubusercontent.com/105893642/202219901-cb27c717-17b6-4892-80cb-a281123cca60.png" width="100px"> |

### Architecture
<img width="1073" alt="finalproject_architecture" src="https://user-images.githubusercontent.com/105893642/202242436-ce3caf9f-aaba-4269-ab4a-dd0ac27e8359.png">



<br>

## 🚀 구현 기능

### ✨ 로그인
<p align="center">
  <img src="https://user-images.githubusercontent.com/105893642/202228738-44b95a11-93af-48e9-b970-7a22d0d11576.png"> 
  로그인 화면
  <br>
</p>

#### 👉 로그인 기능 설명
  1. ID, PW 입력 후 로그인 버튼 활성화.
  2. DB에서 ID, PW 존재여부 검증 후 로그인 성공.

<br>

### ✨ 회원가입
<p align="center">
  <img src="https://user-images.githubusercontent.com/105893642/202229374-ecccddaa-02ef-42c9-9312-326a2585acd1.png"> 
  회원가입 화면
</p>

#### 👉 회원가입 기능 설명
  1. 이름, 이메일, 아이디, 비밀번호를 통해 회원가입.
  2. 한글이름이 아니면 예외 처리 후 가이드 문구 출력. ex) 한글이름이 아닙니다.
  3. 이메일 형식이 올바르지 않으면 예외 처리 후 가이드 문구 출력. ex) 올바른 이메일 형식이 아닙니다.
  4. 이메일 형식이 올바르면 중복체크 버튼 활성화.
  5. 아이디에 특수문자가 포함되거나 5자 미만이면 예외 처리 후 가이드 문구 출력. ex) 특수문자를 제외해여 5자 이상으로 입력해 주세요.
  6. 아이디 형식이 올바르면 중복체크 버튼 활성화.
  7. 중복 체크 버튼 클릭 시 DB에 존재 여부 검증 후 사용 가능(사용 가능한 이메일, 아이디입니다.) 사용 불가(이미 존재하는 아이디, 이메일입니다.)
  8. 특수문자를 포함하여 8자 이상이면 올바른 비밀번호.
  9. 입력된 비밀번호와 동일여부 확인.
  10. 모든 입력값이 정상이면 가입 완료하기 버튼 활성화.
  11. 가입 완료 후 회원가입 안내 메일 발송 후 로그인 페이지로 이동.

<br>

### ✨ 아이디 찾기
<p align="center">
  <img src="https://user-images.githubusercontent.com/105893642/202229952-f9690c4d-9a42-4758-a281-2663fcd44f9f.png"> 
  아이디 찾기 화면
</p>

#### 👉 아이디 찾기 기능 설명
  1. 이름 입력.
  2. 가입한 이메일 입력.
  3. DB에서 존재하는 회원인지 검증 후 마스킹 처리된 아이디 출력. ex) abcd12**
  4. 아이디 전체 보기 버튼 클릭 시 메일로 인증번호 발송.
  5. 인증번호 입력 후 전체 아이디 확인 가능.

<br>

### ✨ 비밀번호 찾기
<p align="center">
  <img src="https://user-images.githubusercontent.com/105893642/202230417-5301f68a-11e7-4e61-8d67-6fcb8734857c.png"> 
  비밀번호 찾기 화면
</p>

#### 👉 비밀번호 찾기 기능 설명
  1. 이름 입력.
  2. 가입한 아이디 입력.
  3. 가입한 이메일 입력.
  4. 이메일 입력 후 인증 버튼 활성화 및 클릭.
  5. 메일로 발송된 인증번호를 제한 시간 안에 입력 시 비밀번호 변경하기 페이지로 이동.

<br>

### ✨ 비밀번호 변경하기
<p align="center">
  <img src="https://user-images.githubusercontent.com/105893642/202230829-37bbd507-8f07-4487-8864-3b68a4298238.png">
  비밀번호 변경하기 화면
</p>

#### 👉 비밀번호 변경하기 기능 설명
  1. 새로운 비밀번호 입력.
  2. 특수문자 포함 8자 이상이면 사용 가능 아니면 사용 불가.
  3. 입력된 비밀번호와 동일여부 확인.
  4. 완료.

<br>

### ✨ 이미지 업로드 및 크롤링
<p align="center">
  <img src="https://user-images.githubusercontent.com/105893642/202231224-8b042dcf-574e-4e25-9a80-6259b7b7c4d0.png">
  이미지 업로드 화면
</p>

#### 👉 이미지 업로드 및 크롤링 기능 설명
  1. 상의, 하의 등 카테고리 별로 이미지 크롤링 후 DB에 저장.
  2. 드레그 앤 드랍으로 이미지 업로드.
  3. 업로드된 이미지와 DB에 저장되어있는 이미지를 AI가 유사도 측정.

<br>

### ✨ 크롤링 결과
<p align="center">
  <img src="https://user-images.githubusercontent.com/105893642/202232393-2a21c32c-06c3-476c-b43f-640e9f53a6c2.png">
  크롤링 결과 화면
</p>

#### 👉 크롤링 결과 기능 설명
  1. 유사도가 높은 순서대로 이미지 리턴.
  2. 카테고리에 맞게 분류 후 유저 화면 출력.

<br>


## 😆 배운 점

<p align="justify">
  팀 프로젝트를 통해 협업 능력, R&R, github 등 다양한 경험을 할 수 있어서 좋았습니다.
  UI/UX를 디자인 및 기획하면서 사용자 친화적인 서비스를 만들 수 있어서 좋은 경험이었습니다. 특히 Login과 관련된 로직을 구현할 때 JWT, AXIOS, 10개 가까이 되는 리액트 모듈을 사용하면서 더욱 안전하고 효과적인 기능을 구현할 수 있어서 좋은 경험이 된 것 같습니다!!
</p>

## 😭 아쉬운 점

<p align="justify">
  AI 모델을 직접 학습시켰지만.. 업로드된 이미지와 크롤링 된 이미지 유사도가 많이 떨어져서 아쉬웠습니다 ㅠㅠ 또한 로그인 시 많이 사용되는 보안 기술인 JWT를 적용시켰지만 Token 관리를 제대로 하지 못한 게 많이 아쉬움이 남습니다ㅠㅠ 좀 더 완벽한 서비스를 만들지 못해 아쉬움이 남습니다 ㅠ
</p>

## 🫡 앞으로 할 일

<p align="justify">
  1. 프로젝트 리팩토링하기. </br>
  2. 로그인 보안기술 제대로 사용하기. </br>
  3. Front 뿐만 아니라 AI, Back 코드 분석하기.
</p>
