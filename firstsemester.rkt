;; n-queens: number -> number
;; Berechnet wieviele Möglichkeiten es gibt, n Damen auf einem n*n Feld zu platzieren, ohne das  2 sich Schlagen können                
;; Example: (n-queens 8) -> 92
;;          (n-queens 4) -> 2
(define (n-queens size)
  (local (
          
 ;;repreäsentiert eine dame an der position x/y
(define-struct dame (x y))


;;do-line: list-of-dame number number->number  
;;Überprüft ob wir am ende sind und genug Damen gesetzt sind, wenn n Damen gesetzt sind wird 1 returnt sonst 0,
;;wenn wir nicht am ende sind, wird die nächste Zeile abgearbeitet  
;;Example: (do-line empty 8 0)->92
 (define (do-line damen n line) 
  (cond
    [(= n line) (if (= (length damen) n) 1 0)] 
    [else (through-line damen n 0 line)]
    )
  )
;;through-line: list-of-dame number number number -> number
;;geht eine zeile durch versucht überall wos geht Damen zu setzen und für jede gesetzte Dame die Möglichkeiten für die Damen der nächsten Zeilen zu ermitteln
;;Beispiel (through-line empty 8 0 0) -> 92
(define (through-line damen n x y)
  (cond
    [(<= n x) 0]
    [(is-free? damen x y) (+ (do-line (cons (make-dame x y) damen) n (+ y 1)) (through-line damen n (+ x 1) y))]
    [else (through-line damen n (+ x 1) y)]
    )
  )

;;is-free?: list-of-dame number number -> boolean
;;überprüft ob eine Dame aus der liste die position x y schlagen kann
;;Beispiel: (is-free? (make-dame 1 1) 2 2) -> false
(define (is-free? damen x y) 
  (foldr 
   ;;list-of-queens boolean -> boolean
   ;;überprüft ob bool true ist oder die Dame d die position x/y schlagen kann
   (lambda (d bool) (and bool 
                               (cond
                                 [(= (dame-x d) x) false]
                                 [(or (= x (+ (dame-x d) (- y (dame-y d)))) (= x (- (dame-x d) (- y (dame-y d))))) false]
                                 [else true]
                                 )
                               )) true damen ))
          )
    (do-line empty size 0)
  )
  )


;; Tests
(check-expect (n-queens 8) 92)
(check-expect (n-queens 4) 2)
