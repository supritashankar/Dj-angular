var myApp = angular.module('myApp',[]);

angular.module('myApp', [],
    function($interpolateProvider) {
        $interpolateProvider.startSymbol('{[');
        $interpolateProvider.endSymbol(']}');
    });    


function BooksListCtrl($scope, $http) {
  $http.get('http://127.0.0.1:8000/books/data/').success(function(data) {
    $scope.bookings = data;
    $scope.name = 'john doe';
  });
}    


angular.module('myApp')
    .directive('helloWorld', function(){
        return {
            restrict: 'E',
            template: '<span>Welcome to the dashboard {{name}}</span>'
        }
});

