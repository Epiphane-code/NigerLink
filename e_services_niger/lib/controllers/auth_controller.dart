import 'package:flutter/material.dart';
import 'package:e_services_niger/services/auth_api.dart';

class AuthController extends ChangeNotifier {
  final Authentification _authService = Authentification();

  bool _isLoading = false;
  bool _isAuthenticated = false;

  String? _error;
  String? _accessToken;
  String? _refreshToken;

  Map<String, dynamic>? _userData;

  bool get isLoading => _isLoading;
  bool get isAuthenticated => _isAuthenticated;
  String? get error => _error;
  String? get accessToken => _accessToken;
  String? get refreshToken => _refreshToken;
  Map<String, dynamic>? get userData => _userData;

  String get user {
    return _userData?['nom']?.toString() ?? '';
  }

  // CONNEXION
  Future<bool> login({required String email, required String password}) async {
    _isLoading = true;
    _error = null;
    notifyListeners();

    try {
      final response = await _authService.login(email, password);

      _saveSession(response);

      if (!_isAuthenticated) {
        _error = 'Token d’accès absent ou invalide.';
      }

      return _isAuthenticated;
    } catch (e) {
      _error = _formatError(e);
      return false;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<bool> register({
    required String nom,
    required String prenom,
    required String email,
    required String proffession,
    required String nationnalite,
    required String sexe,
    required String phone,
    required String deviceId,
    required String deviceName,
    required String password,
    required String pays,
    required String ville,
    required String quartier,
  }) async {
    _isLoading = true;
    _error = null;
    notifyListeners();

    try {
      await _authService.register(
        nom: nom,
        prenom: prenom,
        email: email,
        proffession: proffession,
        nationnalite: nationnalite,
        sexe: sexe,
        phone: phone,
        deviceId: deviceId,
        deviceName: deviceName,
        password: password,
        pays: pays,
        ville: ville,
        quartier: quartier,
      );

      // Si le service ne lève aucune exception,
      // l'inscription est considérée comme réussie.
      return true;
    } catch (e) {
      _error = _formatError(e);
      debugPrint('Erreur inscription : $_error');
      return false;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  // ENREGISTRER LA SESSION
  void _saveSession(Map<String, dynamic> response) {
    _accessToken = response['access_token'] as String?;
    _refreshToken = response['refresh_token'] as String?;

    final data = response['user'];

    if (data is Map<String, dynamic>) {
      _userData = data;
    }

    _isAuthenticated = _accessToken != null && _accessToken!.isNotEmpty;
  }

  // FORMATER LES ERREURS
  String _formatError(Object error) {
    return error.toString().replaceFirst('Exception: ', '');
  }

  // DÉCONNEXION
  void logout() {
    _accessToken = null;
    _refreshToken = null;
    _userData = null;
    _isAuthenticated = false;
    _error = null;

    notifyListeners();
  }
}
