function AddStudentCtrl($scope, $http, $location) {
    $http.get('/api/v1/class/?format=json').
        success(function(classes){
            $scope.classes = classes.objects;
        });

    $scope.submitForm = function() {
        $http.post('/api/v1/student/?format=json', $scope.student).
            success(function(response){
                $location.path("/");
            })
    }
}