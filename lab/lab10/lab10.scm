(define (over-or-under num1 num2) 
    (cond ((< num1 num2) -1)
           ((= num1 num2) 0)
           (else          1)           
    )
)

(define (over-or-under num1 num2) 
    (if (< num1 num2)
        -1
        (if (= num1 num2)
        0
        1
        ) 
    )
)


(define (make-adder num) 
    (lambda (inc) 
        (+ inc num)
    )
)


(define (composed f g) 
    (lambda (x)
        (f (g x))
        )


)

(define lst 
    (list
        (cons 1 nil) 
        2
        (cons 3 (cons 4 nil))
        5
    )
)

(define (remove item lst) 'YOUR-CODE-HERE)
