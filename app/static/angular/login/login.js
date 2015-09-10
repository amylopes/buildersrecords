angular.module('app.login', [

])
.config(function($stateProvider) {
    $stateProvider.state('login', {
        url: '/login',
        templateUrl: 'angular/login/login.html',
        controller: 'LoginController'
    })
})
.controller('LoginController', function(Restangular, $scope, store, $state) {
    store.remove('jwt');

    $scope.redirectToSignup = function() {
        $state.go('signup');
    }
    $scope.redirectToLogin = function() {
        $state.go('login');
    }
    $scope.logIn = function() {
        // Authenticate user
        Restangular.all('auth').post({
            username: $scope.login,
            password: $scope.password
        }).then(function(auth) {
            store.set('jwt', auth.token);
            store.set('signed_user', $scope.login);
            // store.set('signed_user_id', $scope.login);
            console.log('User Authenticated.');
            $state.go('projects');
        });
    }
});
