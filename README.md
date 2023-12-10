# Voice_Recognition_Console_Chess
#### Requiremet
[SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
You can download it by entering the following command in IDE.
```
pip install SpeechRecognition
```

### Outline
The project has made it possible to play chess on the console with just voice.
### Features
- main.py, chess.py, pieces.py 로 이루어져있다.
- main.py 체스 게임의 실행을 담당한다
- chess.py 는 전체적인 움직임 처리와 규칙을 담당한다 
- pieces.py 는 각 말들의 움직임을 담당한다. 
### Chess Rule
#### 행마법
**비숍의 행마법**
대각선으로 원하는 만큼 움직입니다.

**룩의 행마법**
룩은 직선으로 원하는 만큼 움직입니다.

**퀸의 행마법**
퀸은 직선과 대각선으로 원하는 만큼 움직입니다.

**나이트의 행마법**
옆으로 한 칸, 앞으로 두 칸 움직입니다. 또는 옆으로 두 칸, 앞으로 한 칸 움직인다고 말할 수 있습니다. 나이트는 전후좌우 모든 방향으로 이와 같이 움직일 수 있으며, 다른 기물들을 뛰어넘을 수 있습니다.

**폰의 행마법**
시작 포지션에 있을 경우에는 두 칸 직진할 수 있으며, 앞 방향으로 한 칸씩 직진합니다. 옆이나 뒤로는 움직일 수 없습니다. 또한 폰의 바로 앞 칸에 기물이 있을 경우에는 그 폰은 움직일 수 없습니다. 폰은 앞 방향 대각선 방향에 상대 기물이 있을 경우, 그 기물을 잡을 수 있습니다.

**킹의 행마법**
킹은 전후좌우 대각선 어느 방향이로든 한 칸 움직일 수 있습니다.

#### 특수 행마법
**프로모션(promotion)**
자신의 진영에 있던 폰이 상대방진영에 끝까지 도달하게 되면 그 폰은 반드시 같은 색깔의 퀸, 룩, 비숍, 나이트 중의 하나로 바뀌어야 하는데 이것을 프로모션이라 합니다.

**앙파상(en passant)**
시작 포지션의 폰이 두 칸 전진했을 때, 그 전진한 폰의 바로 옆 칸에 인접한 상대 폰은, 방금 두 칸 전진한 폰이 한 칸 움직였다고 간주하고 잡을 수 있습니다. 이렇게 기물을 취하는 방식을 앙파상이라고 일컫습니다. 앙파상은 상대 대국자가 시작 포지션의 폰을 두 칸 움직인 바로 다음 차례에서만 가능합니다.

**캐슬링(castling)**
시작 포지션의 킹이 룩이 있는 쪽을 향하여 두 칸 움직인 경우, 룩이 킹을 뛰어넘어 킹의 바로 옆 칸으로 움직이는 것을 캐슬링이라 하며, 킹과 룩 2개의 기물을 움직였지만 1수로 간주합니다. 오른쪽과 왼쪽 둘다 가능하다.

**캐슬링이 불가능한 조건**
킹과 룩 두 기물 중 하나라도 움직이면 불가능합니다.
캐슬링 하려는 쪽에 기물이 놓여있으면 불가능 합니다.
체크로 킹이 공격받고 있는 상태, 킹의 이동 경로 간 공격을 받고 있는 상태, 캐슬링을 끝마쳤는데 공격을 받는 상태일 경우엔 불가능 합니다.
룩을 먼저 잡고 캐슬링을 하려고 할 경우 이 때는 킹이 아닌 룩을 움직이려는 것으로 간주하고 캐슬링이 불가능 합니다.
출처: [대한체스연맹](http://www.kchess.or.kr/)

### Implementation
1. 처음에는 음성으로 할지 텍스트로 할지 정할 수 있습니다.
2. 움직일 말의 시작위치를 입력하고 다음 끝 위치를 입력하면 됩니다.
3. 다음 사람의 턴으로 넘어갑니다.
#### Voice version
<img src="https://github.com/wingun322/Voice-Recognition-Chess/blob/main/img/Implementation1.JPG">
#### Text version
<img src="https://github.com/wingun322/Voice-Recognition-Chess/blob/main/img/Implementation2.JPG">
#### Implementation Video
https://github.com/wingun322/Voice-Recognition-Chess/blob/main/img/implementation.mp4
