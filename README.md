# Artec3D Test task 
Python + pytest + Selenium

# Install
1. Clone repo to local
`git clone https://github.com/Shakuchi/artec3D_test_python.git`
2. Edit run-configuration for best time
<img width="254" alt="image" src="https://user-images.githubusercontent.com/85437160/206166946-f0614bc1-a050-43aa-b61e-209c8f79e310.png">
<img width="672" alt="image" src="https://user-images.githubusercontent.com/85437160/206167054-bea71df0-65ea-4d94-ae72-e8f869ab2718.png">
3. Run configuration with usage all test files

# Usage
Мы получаем страницу. На странице присутствует ссылка, которая ведёт на следующую страницу. И так далее до последней страницы, на которой написано, что она последняя.
Нужно проверить все страницы (с 1 по последнюю) на наличие ссылок. Если ссылок нет - указать их номера.

Запустив тест, в результате его работы мы получим файл `testResults.txt` в котором будут находится номера страниц без ссылок. 
Таким образом мы сэкономим время для проверки внушительного количества страниц. 
