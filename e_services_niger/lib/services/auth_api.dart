import 'dart:async';
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class Authentification {
  final String urlBase = 'http://192.168.1.222:8000';

  // CONNEXION
  Future<Map<String, dynamic>> login(String email, String password) async {
    final uri = Uri.parse('$urlBase/auth/login');

    final response = await http
        .post(
          uri,
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
          },
          body: jsonEncode({'email': email, 'password': password}),
        )
        .timeout(const Duration(seconds: 15));

    return _handleResponse(response);
  }

  Future<Map<String, dynamic>> register({
    required String nom,
    required String prenom,
    required String email,
    required String proffession,
    required String nationnalite,
    required String sexe,
    required String phone,
    required String? deviceId,
    required String? deviceName,
    required String password,
    required String pays,
    required String ville,
    required String quartier,
  }) async {
    final uri = Uri.parse('$urlBase/auth/register');

    debugPrint('INSCRIPTION : envoi de la requête vers $uri');

    try {
      final response = await http
          .post(
            uri,
            headers: {
              'Content-Type': 'application/json',
              'Accept': 'application/json',
            },
            body: jsonEncode({
              'nom': nom.trim(),
              'prenom': prenom.trim(),
              'email': email.trim(),
              'proffession': proffession.trim(),
              'nationnalite': nationnalite.trim(),
              'sexe': sexe,
              'phone': phone.trim(),
              'deviceId': deviceId,
              'deviceName': deviceName,
              'password': password,
              'pays': pays.trim(),
              'ville': ville.trim(),
              'quartier': quartier.trim(),
            }),
          )
          .timeout(const Duration(seconds: 60));

      debugPrint('INSCRIPTION : statut HTTP ${response.statusCode}');
      debugPrint('INSCRIPTION : réponse ${response.body}');

      return _handleResponse(response);
    } on TimeoutException {
      debugPrint('INSCRIPTION : délai de 60 secondes dépassé');

      throw Exception(
        'Le serveur met trop de temps à répondre. '
        'Vérifiez son état avant de réessayer.',
      );
    } on http.ClientException catch (e) {
      debugPrint('INSCRIPTION : erreur réseau $e');

      throw Exception('Erreur de connexion au serveur : ${e.message}');
    } on FormatException catch (e) {
      debugPrint('INSCRIPTION : erreur JSON $e');

      throw Exception(
        'La réponse du serveur n’est pas au format JSON attendu.',
      );
    }
  }

  Map<String, dynamic> _handleResponse(http.Response response) {
    final dynamic decoded;

    try {
      decoded = jsonDecode(utf8.decode(response.bodyBytes));
    } on FormatException {
      throw Exception(
        'Réponse invalide du serveur '
        '(HTTP ${response.statusCode}).',
      );
    }

    if (decoded is! Map<String, dynamic>) {
      throw Exception('Format de réponse inattendu du serveur.');
    }

    if (response.statusCode >= 200 && response.statusCode < 300) {
      return decoded;
    }

    final detail = decoded['detail'];

    final message = detail is String
        ? detail
        : detail != null
        ? jsonEncode(detail)
        : 'Erreur HTTP ${response.statusCode}';

    throw Exception(message);
  }
}
