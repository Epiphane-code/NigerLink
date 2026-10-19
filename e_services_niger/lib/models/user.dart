class UserModel {
  final int userId;
  final String nom;
  final String prenom;
  final String? email;
  final String proffession;
  final String nationnalite;
  final String sexe;
  final String phone;
  final String? photo;
  final int? deviceId;
  final String? deviceName;
  final String role;
  final String pays;
  final String ville;
  final String quartier;
  UserModel({
    required this.userId,
    required this.nom,
    required this.prenom,
    this.email,
    required this.proffession,
    required this.nationnalite,
    required this.sexe,
    required this.phone,
    this.photo,
    this.deviceId,
    this.deviceName,
    required this.role,
    required this.pays,
    required this.ville,
    required this.quartier
 
  });

      
    factory UserModel.fromMap(Map<String, dynamic> map) {
      return UserModel(
        userId: map['userId'] as int,
        nom: map['nom'] ?? '',
        prenom: map['prenom'] ?? '',
        email: map['email'],
        proffession: map['proffession'] ?? '',
        nationnalite: map['nationnalite'] ?? '',
        sexe: map['sexe'] ?? '',
        phone: map['phone'] ?? '',
        photo: map['photo'],
        deviceId: map['deviceId'],
        deviceName: map['deviceName'],
        role: map['role'] ?? 'citoyen',
        pays: map['pays'] ?? '',
        ville: map['ville'] ?? '',
        quartier: map['quartier'] ?? '',
      );
    }
}
