var myApp = angular.module('myApp',[]);

angular.module('myApp', [],
    function($interpolateProvider) {
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
    });
