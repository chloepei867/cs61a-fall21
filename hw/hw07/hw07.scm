(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (ordered? s) 
    (if (or (null? s) (null? (cdr s)))
        true
        (if (<= (car s) (cadr s))
            (ordered? (cdr s))
            false
        )

    )
)

(define (square x) (* x x))

(define (pow base exp)
    (cond
        ((= exp 0) 1)
        ((= exp 1) base)
        ((even? exp) (square (pow base (/ exp 2))))
        ((* base (square (pow base (quotient exp 2)))))
    )
)
