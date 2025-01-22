;; Примитивы
(println (+ 2 3)) 
(println (* 4 7)) 

;; Строки
(println (str "Hello, " "Clojure!"))

;; Логические значения
(println true)
(println false)

;; Коллекции
;; Списки (List)
(def my-list '(1 2 3 4))
(println (first my-list))
(println (rest my-list))

;; Векторы (Vector)
(def my-vector [1 2 3 4])
(println (nth my-vector 2))

;; Хэши (Maps)
(def my-map {:name "Alice" :age 30})
(println (:name my-map))

;; Множества (Set)
(def my-set #{1 2 3})
(println my-set)

;; Функции
;; Определение функций
(defn greet [name]
  (str "Hello, " name "!"))
(println (greet "Clojure"))

;; Анонимные функции
(println ((fn [x] (* x x)) 5))

;; Высшие функции
(defn apply-func [f x]
  (f x))
(println (apply-func inc 10))

;; Практика работы с Clojure
;; Использование REPL
;; Простые вычисления
(println (+ 10 20))

;; Работа с коллекциями
(def numbers [1 2 3 4])
(println (map #(* % 2) numbers))

;; Практическое задание
;; Задание 1: Удвоение всех элементов списка
(defn double-elements [coll]
  (map #(* % 2) coll))
(println (double-elements [1 2 3])) ;; (2 4 6)

;; Задание 2: Сумма всех чисел в списке
(defn sum-elements [coll]
  (reduce + coll))
(println (sum-elements [1 2 3])) ;; 6
