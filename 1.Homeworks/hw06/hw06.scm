;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  'YOUR-
  (car (cddr s)
  )
)

(define (sign x)
  'YOUR-CODE-HERE
  (cond
  ((< x 0) -1)
  ((= x 0) 0)
  ((> x 0) 1)
  )
)

(define (square x) (* x x))

(define (pow b n)
  'YOUR-CODE-HERE
  (cond
      ((= b 1) 1)
     ((= n 0) 1)
     ((= n 1) b)
    ((even? n) (* (pow b (- n 2)) (square b) ))
    (else (* b (pow b (- n 3)) (square b) ))

  )
)


(define (unique s)
  'YOUR-CODE-HERE
  
)