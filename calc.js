<script src="https://www.desmos.com/api/v1.8/calculator.js?apiKey=dcb31709b452b1cf9dc26972add0fda6"></script>

var elt = document.getElementById('calculator');
var calculator = Desmos.GraphingCalculator(elt);

module.exports = class Calc {
	graphit(x) {
	    calculator.setExpression({
        	id: 'm', latex: x
	    });
	}
}
