
import 'package:flutter/material.dart';
import '../../controllers/auth_controller.dart';

class RegisterPage extends StatefulWidget {
  const RegisterPage({super.key});

  @override
  State<RegisterPage> createState() => _RegisterPageState();
}

class _RegisterPageState extends State<RegisterPage> {
  final _formKey = GlobalKey<FormState>();

  final nom = TextEditingController();
  final prenom = TextEditingController();
  final email = TextEditingController();
  final proffession = TextEditingController();
  final nationnalite = TextEditingController();
  final phone = TextEditingController();
  final password = TextEditingController();
  final passwordconfirme = TextEditingController();
  final pays = TextEditingController();
  final ville = TextEditingController();
  final quartier = TextEditingController();

  final controller = AuthController();

  String? sexeSelectionne;

  bool obscure = true;
  bool obscureConfirmation = true;
  bool loading = false;

  static const couleurPrimaire = Color(0xFF007A4D);

  @override
  void dispose() {
    nom.dispose();
    prenom.dispose();
    email.dispose();
    proffession.dispose();
    nationnalite.dispose();
    phone.dispose();
    password.dispose();
    passwordconfirme.dispose();
    pays.dispose();
    ville.dispose();
    quartier.dispose();

    super.dispose();
  }

  String? champObligatoire(String? value) {
    if (value == null || value.trim().isEmpty) {
      return 'Ce champ est obligatoire.';
    }
    return null;
  }

 
Future<void> register() async {
  if (!_formKey.currentState!.validate()) {
    return;
  }

  if (sexeSelectionne == null) {
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(
        content: Text('Veuillez sélectionner votre sexe.'),
      ),
    );
    return;
  }

  if (password.text != passwordconfirme.text) {
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(
        content: Text('Les mots de passe ne correspondent pas.'),
      ),
    );
    return;
  }

  if (password.text.length < 6) {
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(
        content: Text(
          'Le mot de passe doit contenir au moins 6 caractères.',
        ),
      ),
    );
    return;
  }

  setState(() {
    loading = true;
  });

  try {
    final bool data = await controller.register(
      nom: nom.text.trim(),
      prenom: prenom.text.trim(),
      email: email.text.trim(),
      proffession: proffession.text.trim(),
      nationnalite: nationnalite.text.trim(),
      sexe: sexeSelectionne!,
      phone: phone.text.trim(),
      deviceId: "",
      deviceName: "",
      password: password.text,
      pays: pays.text.trim(),
      ville: ville.text.trim(),
      quartier: quartier.text.trim(),
    );

    debugPrint('Résultat inscription : $data');

    if (!mounted) return;

    if (data == true) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Compte créé avec succès.'),
          backgroundColor: couleurPrimaire,
        ),
      );

      Navigator.pop(context);
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text(
            'Échec de l’inscription. Vérifiez la réponse du serveur.',
          ),
          backgroundColor: Colors.red,
        ),
      );
    }
  } catch (e, stackTrace) {
    debugPrint('Erreur inscription : $e');
    debugPrintStack(stackTrace: stackTrace);

    if (!mounted) return;

    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(
          'Erreur lors de l’inscription : '
          '${e.toString().replaceFirst('Exception: ', '')}',
        ),
        backgroundColor: Colors.red,
      ),
    );
  } finally {
    if (mounted) {
      setState(() {
        loading = false;
      });
    }
  }
}


  Widget champTexte({
    required TextEditingController controller,
    required String label,
    required IconData icon,
    TextInputType keyboardType = TextInputType.text,
    String? Function(String?)? validator,
    TextCapitalization textCapitalization = TextCapitalization.none,
  }) {
    return TextFormField(
      controller: controller,
      keyboardType: keyboardType,
      textCapitalization: textCapitalization,
      textInputAction: TextInputAction.next,
      validator: validator ?? champObligatoire,
      decoration: InputDecoration(
        labelText: label,
        prefixIcon: Icon(icon),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(14),
        ),
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(14),
          borderSide: BorderSide(color: Colors.grey.shade400),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(14),
          borderSide: const BorderSide(
            color: couleurPrimaire,
            width: 2,
          ),
        ),
      ),
    );
  }

  Widget champMotDePasse({
    required TextEditingController controller,
    required String label,
    required bool obscureText,
    required VoidCallback onToggle,
    String? Function(String?)? validator,
  }) {
    return TextFormField(
      controller: controller,
      obscureText: obscureText,
      textInputAction: TextInputAction.next,
      validator: validator ?? champObligatoire,
      decoration: InputDecoration(
        labelText: label,
        prefixIcon: const Icon(Icons.lock_outline_rounded),
        suffixIcon: IconButton(
          onPressed: onToggle,
          icon: Icon(
            obscureText
                ? Icons.visibility_outlined
                : Icons.visibility_off_outlined,
          ),
        ),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(14),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(14),
          borderSide: const BorderSide(
            color: couleurPrimaire,
            width: 2,
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Créer un compte'),
        foregroundColor: couleurPrimaire,
      ),
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.fromLTRB(24, 12, 24, 30),
          child: Form(
            key: _formKey,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                const Icon(
                  Icons.person_add_alt_1_rounded,
                  size: 65,
                  color: couleurPrimaire,
                ),

                const SizedBox(height: 12),

                const Text(
                  'Bienvenue sur NigerLink',
                  textAlign: TextAlign.center,
                  style: TextStyle(
                    fontSize: 22,
                    fontWeight: FontWeight.w800,
                  ),
                ),

                const SizedBox(height: 8),

                Text(
                  'Créez votre compte pour accéder aux services.',
                  textAlign: TextAlign.center,
                  style: TextStyle(color: Colors.grey.shade700),
                ),

                const SizedBox(height: 25),

                champTexte(
                  controller: nom,
                  label: 'Nom',
                  icon: Icons.person_outline,
                  textCapitalization: TextCapitalization.words,
                ),

                const SizedBox(height: 14),

                champTexte(
                  controller: prenom,
                  label: 'Prénom',
                  icon: Icons.person_outline_rounded,
                  textCapitalization: TextCapitalization.words,
                ),

                const SizedBox(height: 14),

                champTexte(
                  controller: email,
                  label: 'Adresse e-mail',
                  icon: Icons.email_outlined,
                  keyboardType: TextInputType.emailAddress,
                  validator: (value) {
                    if (value == null || value.trim().isEmpty) {
                      return 'L’adresse e-mail est obligatoire.';
                    }

                    final emailValide = RegExp(
                      r'^[^@\s]+@[^@\s]+\.[^@\s]+$',
                    ).hasMatch(value.trim());

                    if (!emailValide) {
                      return 'Veuillez saisir une adresse e-mail valide.';
                    }

                    return null;
                  },
                ),

                const SizedBox(height: 14),

                champTexte(
                  controller: proffession,
                  label: 'Profession',
                  icon: Icons.work_outline,
                  textCapitalization: TextCapitalization.words,
                ),

                const SizedBox(height: 14),

                champTexte(
                  controller: nationnalite,
                  label: 'Nationalité',
                  icon: Icons.flag_outlined,
                  textCapitalization: TextCapitalization.words,
                ),

                const SizedBox(height: 14),

                DropdownButtonFormField<String>(
                  value: sexeSelectionne,
                  decoration: InputDecoration(
                    labelText: 'Sexe',
                    prefixIcon: const Icon(Icons.wc_rounded),
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(14),
                    ),
                  ),
                  items: const [
                    DropdownMenuItem(
                      value: 'Masculin',
                      child: Text('Masculin'),
                    ),
                    DropdownMenuItem(
                      value: 'Féminin',
                      child: Text('Féminin'),
                    ),
                  ],
                  onChanged: loading
                      ? null
                      : (value) {
                          setState(() {
                            sexeSelectionne = value;
                          });
                        },
                ),

                const SizedBox(height: 14),

                champTexte(
                  controller: phone,
                  label: 'Téléphone',
                  icon: Icons.phone_outlined,
                  keyboardType: TextInputType.phone,
                ),

                const SizedBox(height: 14),

                champTexte(
                  controller: pays,
                  label: 'Pays',
                  icon: Icons.public_rounded,
                  textCapitalization: TextCapitalization.words,
                ),

                const SizedBox(height: 14),

                champTexte(
                  controller: ville,
                  label: 'Ville',
                  icon: Icons.location_city_rounded,
                  textCapitalization: TextCapitalization.words,
                ),

                const SizedBox(height: 14),

                champTexte(
                  controller: quartier,
                  label: 'Quartier',
                  icon: Icons.location_on_outlined,
                  textCapitalization: TextCapitalization.words,
                ),

                const SizedBox(height: 14),

                champMotDePasse(
                  controller: password,
                  label: 'Mot de passe',
                  obscureText: obscure,
                  onToggle: () {
                    setState(() {
                      obscure = !obscure;
                    });
                  },
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Le mot de passe est obligatoire.';
                    }

                    if (value.length < 6) {
                      return 'Minimum 6 caractères.';
                    }

                    return null;
                  },
                ),

                const SizedBox(height: 14),

                champMotDePasse(
                  controller: passwordconfirme,
                  label: 'Confirmer le mot de passe',
                  obscureText: obscureConfirmation,
                  onToggle: () {
                    setState(() {
                      obscureConfirmation = !obscureConfirmation;
                    });
                  },
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Veuillez confirmer votre mot de passe.';
                    }

                    if (value != password.text) {
                      return 'Les mots de passe ne correspondent pas.';
                    }

                    return null;
                  },
                ),

                const SizedBox(height: 25),

                SizedBox(
                  height: 52,
                  child: FilledButton(
                    onPressed: loading ? null : register,
                    style: FilledButton.styleFrom(
                      backgroundColor: couleurPrimaire,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(14),
                      ),
                    ),
                    child: loading
                        ? const SizedBox(
                            width: 24,
                            height: 24,
                            child: CircularProgressIndicator(
                              strokeWidth: 2.5,
                              color: Colors.white,
                            ),
                          )
                        : const Text(
                            'S’inscrire',
                            style: TextStyle(
                              fontWeight: FontWeight.w800,
                            ),
                          ),
                  ),
                ),

                const SizedBox(height: 20),

                TextButton(
                  onPressed: loading
                      ? null
                      : () => Navigator.pop(context),
                  child: const Text(
                    'Vous avez déjà un compte ? Se connecter',
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
